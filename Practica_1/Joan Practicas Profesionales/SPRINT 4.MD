# Sprint Report Semanal (24 de febrero - 28 de febrero)

## Información

| Campo | Valor |
|-------|-------|
| **Proyecto** | GTI Digital Twin — Visualización de Drones |
| **Semana** | #4 (Fecha: 24 al 28 de Febrero) |
| **Fase** | 1: Telemetry Foundation |
| **Practicante** | Joan Carlos Monfil Huitle (Backend & Robotics) |

---

## ✅ Lo que hice esta semana

- [x] **Story 1.3:** Durante este sprint se logró la integración funcional entre el backend de telemetría y el frontend de visualización del Digital Twin. Uniendo el trabajo que cada uno hizo de manera independiente, donde
al inicio de la semana se empezo realizando un pequeño testing al trabajo de cada uno, donde principalemnte fue para ver si marcaban errores de manera independiente.
  - Implementación de ambos sitemas, backend y front.
  - Testing independiente para visualizar posibles fallos al funcionar solos. 
  - Correcion de errores al momento de unirlos. 
  - Modificacion de codigo y lineas, cambiando algunas variables como al igual configuraciones independientes. 
  - Implementación de vista, donde se visualiza el dron en el mapa de front.
  - Validación de ambos miembros, 
- [x] **Testing:** Se realizo diferentes pruebas y modificaciones a los codigos creados e implementados, como al igual 
se depuraron errores significativos que se tenian en su momento. 
  - Reinicio completo del sistema desde cero (SITL + QGC + Bridge).
  - Verificación de generación automática de `run_id`.
  - Reinicio de pagina del front, y al igual de todo el codigo, multiples pruebas. 
  - Validación de actualización en tiempo real en Supabase.
  - Validación de actualización en tiempo real de los datos del backend con el front. 
  - Pruebas de detención limpia mediante `Ctrl+C`.
- [x] **Docs:** Union de backend y front, donde el front recibe los datos de backend y estos mismos los muestra en pantalla.

**PRs creados/mergeados:**
- PR #: Codigos creados y modificados, mismos guardados por front. — Estado: En review/operational.

**Horas aproximadas trabajadas:** 22h

---

## 🎯 Lo que haré la próxima semana

- [ ] **Story 1.3:** Pruebas de integracion basado alas tareas de Backend/Robotics ( 24 al 28 de Febrero).
- [ ] **Apoyo a Story 1.4:** Ayudar a aclarar posibles dudas sobre las tareas realizadas por backend y union del front. 
- [ ] **Optimización:** Seguir familiarizando con MAVLink, SITL, QGC, WSL, Supabase, Antigravaty, y Github para mejor control de datos y codigods e ir avanzando poco a poco con los proximos story y epics.
- [ ] **Preparar** GitHub, Vercel y proximas tareas, investigar lo que toca hacer.

---

## 🚧 Bloqueos / Impedimentos

| Bloqueo | Impacto | Necesito |
|---------|---------|----------|
| Problemas con las aplicaciones y múltiples desfaces de información. | Entorpeció la tarea principal. | Realiza un análisis de lo que he estado realizando. |
|Errores de codigo. | Relantizacion de avance | Considerar los demás rubros para tener el menor número de fallas. |

---

## 🆘 Lo que necesito

- [ ] Revisar Tabla `drone_telemetry`.
- [ ] Verificar el `Telemetry Bridge (Python + pymavlink)`.
- [ ] Entender mejor lo que hace el front.
- [ ] Trabajar al 100% con GitHub, respecto a los branch, pero creo que lo logre. 
- [ ] Respecto a la union del front con el backend, revisar las variables por posibles choques.
- [ ] Nada más — todo bien 👍

---

## 💡 Aprendizajes / Notas

- Las cosas llevan mas tiempo de lo esperado. 
- Comprender mejor los puentes de comunicacion como al igual codigos. 
- Es bueno saber que hace el demas equipo aunque no se te asigne esa tarea y tener una idea. 
- Sugerencia: Considerar errores y tiempo invertido en dichos errores para no retrasar las tareas pendientes.
- Trabajar y poner un poco mas de atencion a las herramientas.
- Tener mas comunicacion con el equipo pero sobretodo dar ideas funcionales.


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
