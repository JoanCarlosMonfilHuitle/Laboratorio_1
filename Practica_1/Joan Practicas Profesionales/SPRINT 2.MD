# Sprint Report Semanal — Template

# Ejemplo Completo (Para Referencia)

## Información

| Campo | Valor |
|-------|-------|
| **Proyecto** | GTI Digital Twin — Visualización de Drones |
| **Semana** | #2 (Fecha: 3 al 7 de Febrero) |
| **Fase** | 1: Telemetry Foundation |
| **Practicante** | Joan Carlos Monfil Huitle (Backend & Robotics) |

---

## ✅ Lo que hice esta semana

- [x] **Story 1.3:** Diseñe, e implementó la infraestructura base de telemetría para el sistema de drones, donde se dejo lista una base de datos capaz de recibir, almacenar y consultar datos de telemetría provenientes de un dron (real o simulado).
  - Creación de la tabla `drone_telemetry` en Supabase (PostgreSQL).
  - Definición de columnas alineadas con mensajes reales de MAVLink.
  - Inserción y verificación de registros de prueba.
  - Configuración de Row Level Security (RLS).
  - Creación de un índice.
  - Validación visual de datos almacenados correctamente.
- [x] **Testing:** Termine el Sprint 1 de la primera semana, donde tuve que realizar muchas modificaciones y consultas independientes. 
- [x] **Docs:** Cree la tabla `drone_telemetry`: [Supabase Project URL](https://vjpaexngmtlcsbzopvam.supabase.co) en Supabase (schema + RLS).

**PRs creados/mergeados:**
- PR #: Tabla `drone_telemetry` — Estado: En review.

**Horas aproximadas trabajadas:** 17h

---

## 🎯 Lo que haré la próxima semana

- [ ] **Story 1.3:** Implementar Telemetry Bridge (09 al 13 de Febrero).
- [ ] **Apoyo a Story 1.4:** Ayudar a aclarar posibles dudas sobre la tabla `drone_telemetry` e incluso modificar algunas observaciones. 
- [ ] **Optimización:** Seguir familiarizando con MAVLink, SITL, QGC y WSL e implemetar un puente de telemetría.
- [ ] **Preparar** Supabse y puente de telemetría.

---

## 🚧 Bloqueos / Impedimentos

| Bloqueo | Impacto | Necesito |
|---------|---------|----------|
| Paginas muy extensas y con informacion poca practica. | Ralentizo la comprencion de que se debe hacer. | Informacion que sea mas sencilla de interpretar y realizar algunos ejemplos independientes. |
|No sabia definir que colocar en las columnas. | Tiempo no muy bien invertido y relantizacion de avance | Tener un enfoque especifico de lo que se debe cumplir o tener como producto final. |
|No entendi del todo algunos atajos o herramientas que se utilizan para estas aplicaciones usadas. | Relantiza mi proceso de entendiemeinto. | Practicar mas. |

---

## 🆘 Lo que necesito

- [ ] Leer protocolos MAVLink.
- [ ] Revisar Tabla `drone_telemetry`.
- [ ] Implementar el puente de telemetría
- [ ] Familiarizarme mas con los programas.
- [ ] Nada más — todo bien 👍

---

## 💡 Aprendizajes / Notas

- Las cosas llevan mas tiempo de lo esperado. 
- No quedarse solo con la informacion que se tiene, esto aplica tambien para herramientas.
- Sugerencia: Tener diversas opcion de investigacion y de como hacer algunas tareas. 

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
