# Sprint Report Semanal (10 de febrero - 14 de febrero)

## Información

| Campo | Valor |
|-------|-------|
| **Proyecto** | GTI Digital Twin — Visualización de Drones |
| **Semana** | #3 (Fecha: 10 al 14 de Febrero) |
| **Fase** | 1: Telemetry Foundation |
| **Practicante** | Joan Carlos Monfil Huitle (Backend & Robotics) |

---

## ✅ Lo que hice esta semana

- [x] **Story 1.3:** Implementé y validé el pipeline completo de telemetría en tiempo real (MAVLink → Python Bridge → Supabase), asegurando una ingestión estable y estructurada de datos provenientes del dron simulado (SITL).
  - Configuración de salida MAVLink adicional (udp:127.0.0.1:14551) para permitir la conexion (QGC + Bridge).
  - Desarrollo del `telemetry_bridge.py` para capturar mensajes MAVLink clave:
    - `HEARTBEAT` 
    - `ATTITUDE`
    - `GLOBAL_POSITION_INT`
    - `VFR_HUD`
    - `SYS_STATUS`
  - Implementación de sistema de snapshot por segundo, evitando inserciones masivas por mensaje individual.
  - Creación automática de un `run_id` (UUID) por sesión para evitar mezcla de datos entre ejecuciones.
  - Inserción estructurada de snapshots completos en la tabla `drone_telemetry`.
  - Implementación de vista SQL `latest_snapshot` para obtener el estado más reciente del dron automáticamente.
  - Implementación de vista `latest_snapshot_mapbox` con conversión de lat/lon (int32 MAVLink → grados decimales) lista para visualización en Mapbox.
  - Validación dinámica del sistema mediante pruebas en QGroundControl (armado, takeoff y movimiento).
- [x] **Testing:** Se realizo diferentes pruebas y modificaciones a los codigos creados e implementados.
  - Reinicio completo del sistema desde cero (SITL + QGC + Bridge).
  - Verificación de generación automática de `run_id`.
  - Confirmación de inserción continua de snapshots.
  - Validación de actualización en tiempo real en Supabase.
  - Pruebas de detención limpia mediante `Ctrl+C`.
  - Confirmación de separación correcta entre sesiones.
- [x] **Docs:** Implemente `Telemetry Bridge (Python + pymavlink)`, donde este recibe MAVLink de SITL y escribe a Supabase, creando codigo en WSL y SQL en Supabase.

## 🔌 telemetry_bridge.py

Este script implementa el puente de telemetría entre MAVLink y Supabase.
Captura mensajes clave del dron, consolida un snapshot por segundo y los almacena en la base de datos con un `run_id` único por sesión.

```python
import os
import time
import uuid
from pymavlink import mavutil
from supabase import create_client, Client
from dotenv import load_dotenv

# =========================
# CARGAR .env
# =========================
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")  # service role key

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Faltan variables SUPABASE_URL o SUPABASE_SERVICE_KEY en tu .env")
    raise SystemExit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# =========================
# CONEXIÓN MAVLINK
# =========================
# Este puerto debe agregarse en MAVProxy:
# output add udp:127.0.0.1:14551
MAVLINK_UDP = os.getenv("MAVLINK_UDP", "udp:127.0.0.1:14551")

print(f"🔌 Conectando a MAVLink en {MAVLINK_UDP} ...")
master = mavutil.mavlink_connection(MAVLINK_UDP)

master.wait_heartbeat()
print("✅ Heartbeat recibido")

# Generar identificador único de sesión
RUN_ID = str(uuid.uuid4())
print(f"🧾 RUN_ID: {RUN_ID}")

# =========================
# LOOP PRINCIPAL
# =========================
MSG_TYPES = [
    "HEARTBEAT",
    "ATTITUDE",
    "GLOBAL_POSITION_INT",
    "VFR_HUD",
    "SYS_STATUS"
]

# =========================
# CACHE (último valor recibido)
# =========================
latest = {
    "system_status": None,
    "roll_x": None,
    "pitch_y": None,
    "yaw_z": None,
    "lat": None,
    "lon": None,
    "alt_msl_mm": None,
    "alt_rel_mm": None,
    "vx": None,
    "vy": None,
    "vz": None,
    "groundspeed_ms": None,
    "heading_deg": None,
    "throttle_pct": None,
    "battery_voltage_mv": None,
    "battery_current_ca": None,
    "battery_remaining_pct": None,
}

last_insert_ts = 0.0
INSERT_EVERY_SEC = 1.0  # 1 snapshot por segundo

try:
    while True:
        msg = master.recv_match(type=MSG_TYPES, blocking=True)
        if not msg:
            continue

        data = msg.to_dict()
        msg_type = msg.get_type()

        # HEARTBEAT
        if msg_type == "HEARTBEAT":
            latest["system_status"] = data.get("system_status")

        # ATTITUDE
        elif msg_type == "ATTITUDE":
            latest["roll_x"] = data.get("roll")
            latest["pitch_y"] = data.get("pitch")
            latest["yaw_z"] = data.get("yaw")

        # GLOBAL_POSITION_INT
        elif msg_type == "GLOBAL_POSITION_INT":
            latest["lat"] = data.get("lat")
            latest["lon"] = data.get("lon")
            latest["alt_msl_mm"] = data.get("alt")
            latest["alt_rel_mm"] = data.get("relative_alt")
            latest["vx"] = data.get("vx")
            latest["vy"] = data.get("vy")
            latest["vz"] = data.get("vz")

        # VFR_HUD
        elif msg_type == "VFR_HUD":
            latest["groundspeed_ms"] = data.get("groundspeed")
            latest["heading_deg"] = data.get("heading")
            latest["throttle_pct"] = data.get("throttle")

        # SYS_STATUS
        elif msg_type == "SYS_STATUS":
            latest["battery_voltage_mv"] = data.get("voltage_battery")
            latest["battery_current_ca"] = data.get("current_battery")
            latest["battery_remaining_pct"] = data.get("battery_remaining")

        # Insertar 1 vez por segundo (snapshot)
        now = time.time()
        if now - last_insert_ts >= INSERT_EVERY_SEC:
            row = {
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "run_id": RUN_ID
            }
            row.update(latest)

            try:
                supabase.table("drone_telemetry").insert(row).execute()
                print("📤 Insertado: snapshot")
                last_insert_ts = now
            except Exception as e:
                print("❌ Error insertando en Supabase:", e)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Detenido por el usuario (Ctrl+C).")
```
## 🗄 Supabase SQL – Índices y Vistas (Sprint 2)

A continuación se muestran los comandos SQL utilizados en Supabase para mejorar rendimiento, separar sesiones de telemetría y exponer endpoints “listos para consumo” (por ejemplo Mapbox).

---

### ✅ CÓDIGO 1 — Índice por `created_at` (consultas rápidas por tiempo)

Este índice acelera las consultas que ordenan por el registro más reciente, especialmente cuando se usa `ORDER BY created_at DESC` para visualizar los últimos snapshots de telemetría.

```sql
create index if not exists drone_telemetry_created_at_idx
on public.drone_telemetry (created_at desc);
```

---

### ✅ CÓDIGO 2 — `run_id` por sesión + índice compuesto (no mezclar datos)

Se agrega la columna `run_id` para etiquetar cada ejecución del bridge como una sesión única.  
El índice `(run_id, created_at DESC)` permite consultar eficientemente los snapshots de una sesión específica sin mezclar datos de otras corridas.

```sql
alter table public.drone_telemetry
add column if not exists run_id uuid;

create index if not exists idx_drone_telemetry_run_id_created_at
on public.drone_telemetry (run_id, created_at desc);
```

---

### ✅ CÓDIGO 3 — Consulta por sesión (debug / verificación)

Este query permite inspeccionar los últimos 20 registros de una sesión específica usando su `run_id`.  
Es útil para verificar rápidamente que el bridge está insertando snapshots correctamente y sin mezclar sesiones.

```sql
select created_at, run_id, lat, lon, groundspeed_ms, battery_remaining_pct
from public.drone_telemetry
where run_id = 'c1e31e56-6046-463b-ab39-6740a6c90320'
order by created_at desc
limit 20;
```

---

### ✅ CÓDIGO 4 — Vista `latest_snapshot` (estado actual automático)

Esta vista retorna **un solo registro**: el snapshot más reciente de la sesión más reciente.  
Sirve para que el frontend o las pruebas consulten “el estado actual del dron” sin tener que copiar manualmente el `run_id`.

```sql
create or replace view public.latest_snapshot as
select *
from public.drone_telemetry
where run_id = (
  select run_id
  from public.drone_telemetry
  where run_id is not null
  order by created_at desc
  limit 1
)
order by created_at desc
limit 1;
```

Verificación rápida:

```sql
select created_at, run_id, lat, lon, groundspeed_ms, battery_remaining_pct
from public.latest_snapshot;
```

---

### ✅ CÓDIGO 5 — Vista `latest_snapshot_mapbox` (Mapbox-ready)

MAVLink entrega `lat` y `lon` como enteros escalados (`* 1e7`).  
Esta vista convierte automáticamente a grados decimales (`lat_deg`, `lon_deg`) y expone el último estado listo para consumir en Mapbox (o cualquier mapa).

```sql
create or replace view public.latest_snapshot_mapbox as
select
  created_at,
  run_id,
  (lat / 1e7::double precision) as lat_deg,
  (lon / 1e7::double precision) as lon_deg,
  heading_deg,
  groundspeed_ms,
  battery_remaining_pct
from public.latest_snapshot;
```

**PRs creados/mergeados:**
- PR #: Codigos `Telemetry Bridge (Python + pymavlink)` — Estado: En review/operational.

**Horas aproximadas trabajadas:** 25h

---

## 🎯 Lo que haré la próxima semana

- [ ] **Story 1.3:** Pruebas de integracion basado alas tareas de Backend/Robotics (16 al 20 de Febrero).
- [ ] **Apoyo a Story 1.4:** Ayudar a aclarar posibles dudas sobre la tabla `drone_telemetry` Y `Telemetry Bridge`. 
- [ ] **Optimización:** Seguir familiarizando con MAVLink, SITL, QGC, WSL, Supabase, Antigravaty e ir avanzando poco a poco con los proximos story y epics.
- [ ] **Preparar** Supabase a posibles cambios y Antigravity.

---

## 🚧 Bloqueos / Impedimentos

| Bloqueo | Impacto | Necesito |
|---------|---------|----------|
| Falla de conexión. | Ralentizo mi avance en el sprint de la semana. | Realiza un posible instructivo para el arranque y posibles fallas. |
| Problemas con las aplicaciones y múltiples desfaces de información. | Entorpeció la tarea principal. | Realiza un análisis de lo que he estado realizando. |
|Errores de codigo. | Tiempo no muy bien invertido y relantizacion de avance | Considerar los demás rubros para tener el menor número de fallas. |
|Modificaciones en Supabase y agregación de codigos. | Relantiza el avance del sprint. | Conocer mejor mi estructura de codigo y entender mejor el funcionamiento de las herrameintas. |

---

## 🆘 Lo que necesito

- [ ] Entender mas Supabase, sobretodo algunos atajos.
- [ ] Revisar Tabla `drone_telemetry`.
- [ ] Verificar el `Telemetry Bridge (Python + pymavlink)`.
- [ ] Familiarizarme con Antigravity.
- [ ] Hacer un seguimiento de arranque.
- [ ] Nada más — todo bien 👍

---

## 💡 Aprendizajes / Notas

- Las cosas llevan mas tiempo de lo esperado. 
- El que halla salido una vez, no significa que salga al segundo intento. 
- Comprender mejor los puentes de comunicacion como al igual codigos. 
- Sugerencia: Considerar errores y tiempo invertido en dichos errores para no retrasar las tareas pendientes.

---

## 📊 Estado General

| Indicador | Estado |
|-----------|--------|
| **¿Estoy al día con el roadmap?** | 🟢 Sí |
| **¿Tengo bloqueos activos?** | 🟡 Si |
| **¿Necesito ayuda?** | 🟡 Si |
| **Confianza en la entrega de la fase** | 🟢 Alta |

---

*Template creado para el Proyecto Digital Twin GTI — Prácticas UDLAP 2026*
