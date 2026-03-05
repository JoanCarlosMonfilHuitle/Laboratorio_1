# Drone Telemetry Pipeline  
SITL → MAVLink → Telemetry Bridge → Supabase

Sistema de simulación y captura de telemetría para drones utilizando **ArduPilot SITL**, **MAVLink**, **QGroundControl** y un **Telemetry Bridge en Python** que almacena datos en **Supabase**.

Este sistema permite:

- Simular un dron con **SITL**
- Visualizar el dron en **QGroundControl**
- Capturar telemetría vía **MAVLink**
- Guardar telemetría en **Supabase**
- Consultar el estado actual del dron desde una base de datos

---

# Arquitectura del sistema

```
ArduPilot SITL
      │
      │ MAVLink
      ▼
MAVProxy
      │
      ├── UDP 14550 → QGroundControl
      │
      └── UDP 14551 → Telemetry Bridge (Python)
                          │
                          ▼
                       Supabase
                          │
                          ▼
                latest_snapshot_mapbox
```

---

# Requisitos

Antes de comenzar asegúrate de tener instalado:

- WSL
- Ubuntu en WSL
- ArduPilot SITL
- QGroundControl
- Python 3
- entorno virtual (`venv`)
- cuenta en Supabase
- proyecto `telemetry_bridge`

---

# Paso 1 — Abrir WSL

Abrir una nueva terminal en Windows.

Ejecutar:

```bash
wsl
```

Debe aparecer algo similar a:

```bash
joancarlos@victus-Joan:~
```

Esto confirma que **WSL está funcionando correctamente**.

![Inicialización WSL](screenshots/inicializacion_wsl.png)

---

# Paso 2 — Iniciar SITL correctamente

Ir a la raíz de ArduPilot:

```bash
cd ~/ardupilot
```

Ahora ejecutar:

```bash
./Tools/autotest/sim_vehicle.py -v ArduCopter --console --map
```

Este comando:

- compila ArduPilot (si es necesario)
- inicia MAVProxy
- abre la consola
- abre el mapa

Debe aparecer algo como:

```
STABILIZE>
```

⚠ **No cerrar esta terminal.**

![Inicio SITL](screenshots/iniciar_sitl.png)

---

# Paso 3 — Configurar salida MAVLink

Dentro de la consola de MAVProxy escribir:

```
output
```

Si aparece algo como:

```
0: 172.18.xxx.xxx:14550
```

Esto significa que solo está conectado **QGroundControl**.

Ahora agregar salida para el bridge:

```
output add udp:127.0.0.1:14551
```

Luego verificar nuevamente:

```
output
```

Debe mostrar:

```
0: 172.18.xxx.xxx:14550
1: udp:127.0.0.1:14551
```

Ahora MAVLink enviará datos tanto a **QGroundControl** como a tu **Telemetry Bridge**.

![Configuración MAVLink](screenshots/configurar_mavlink.png)

---

# Paso 4 — Abrir QGroundControl

Abrir **QGroundControl** en Windows.

El sistema debe:

- conectarse automáticamente
- mostrar el dron en el mapa

Confirmar que aparece:

```
Ready to Fly
```

![QGroundControl](screenshots/abrir_qgc.png)

---

# Paso 5 — Iniciar Telemetry Bridge

Abrir **una nueva terminal**.

Entrar al proyecto:

```bash
wsl
cd ~/telemetry_bridge
```

Activar entorno virtual:

```bash
source venv/bin/activate
```

Ejecutar el bridge:

```bash
python3 telemetry_bridge.py
```

Debe mostrar algo como:

```
Conectando a MAVLink...
Heartbeat recibido
RUN_ID: xxxxx
Insertado: snapshot
Insertado: snapshot
```

Dejar correr **5–10 segundos**.

![Telemetry Bridge](screenshots/iniciar_bridge.png)

---

# Paso 6 — Verificar en Supabase

Ir a:

```
Supabase → SQL Editor → Nueva Query
```

Ejecutar:

```sql
select * from public.latest_snapshot_mapbox;
```

Debe devolver **una fila con datos** como:

- lat_deg
- lon_deg
- groundspeed_ms
- battery_remaining_pct

![Consulta Supabase](screenshots/verificar_supabase.png)

---

# Paso 7 — Prueba dinámica

En **QGroundControl**:

1. Cambiar modo a **GUIDED**
2. Presionar **ARM**
3. Ejecutar **Takeoff**

Después verificar en Supabase que cambian los valores:

- alt_rel_mm
- groundspeed_ms
- lat_deg
- lon_deg

Esto confirma que la telemetría fluye correctamente.

![Prueba dinámica](screenshots/prueba_dinamica.png)

---

# Paso 8 — Detener el sistema correctamente

Para detener el sistema:

En la terminal del **bridge**:

```
Ctrl + C
```

En la terminal de **SITL**:

```
Ctrl + C
```

Cerrar **QGroundControl**.

![Detener sistema](screenshots/detener_sistema.png)

---

# Resultado esperado final

Al completar todos los pasos:

- SITL corre correctamente
- QGroundControl se conecta
- Telemetry Bridge imprime snapshots
- Supabase recibe datos
- `latest_snapshot_mapbox` refleja movimiento del dron

Sistema completo funcional.

---

# Problemas comunes

## QGroundControl no conecta

Verificar que SITL esté corriendo y que el puerto **14550** esté activo.

---

## El bridge no recibe datos

Verificar la salida MAVLink:

```
output
```

Debe aparecer:

```
udp:127.0.0.1:14551
```

---

## Supabase no recibe datos

Verificar:

- variables de entorno
- conexión a internet
- permisos de tabla

---

# Licencia

Uso académico y experimental.
