# Sprint Report Semanal — Template
---

# Ejemplo Completo (Para Referencia)

> Así se ve un sprint report lleno. Úsenlo como guía.

---

## Información

| Campo | Valor |
|-------|-------|
| **Proyecto** | GTI Digital Twin — Visualización de Drones |
| **Semana** | #3 (Fecha: 10 al 14 de febrero) |
| **Fase** | 1: Telemetry Foundation |
| **Practicante** | Juan Pérez (Backend & Robotics) |

---

## ✅ Lo que hice esta semana

- [x] **Story 1.3:** Implementé el Telemetry Bridge en Python
  - Escucha UDP en puerto 14551 con pymavlink
  - Parsea los 5 mensajes clave (HEARTBEAT, GLOBAL_POSITION_INT, ATTITUDE, VFR_HUD, SYS_STATUS)
  - Normaliza datos y hace upsert a Supabase con rate limiting a 5Hz
- [x] **Testing:** Conecté el bridge a SITL y verifiqué que los datos llegan a Supabase correctamente
- [x] **Docs:** Escribí el README del bridge con instrucciones de setup

**PRs creados/mergeados:**
- PR #7: `feat: implement telemetry bridge service` — Estado: en review

**Horas aproximadas trabajadas:** 22h

---

## 🎯 Lo que haré la próxima semana

- [ ] **Story 1.3:** Resolver feedback del PR (si hay)
- [ ] **Apoyo a Story 1.4:** Ayudar a María con la verificación de que los datos llegan al frontend
- [ ] **Optimización:** Agregar structured logging al bridge
- [ ] **Preparar** demo de pipeline completo para Sprint Review del viernes

---

## 🚧 Bloqueos / Impedimentos

| Bloqueo | Impacto | Necesito |
|---------|---------|----------|
| SITL tarda ~2 min en arrancar cada vez | Ralentiza ciclos de prueba | Ver si hay forma de persistir el estado (menor, no crítico) |

---

## 🆘 Lo que necesito

- [ ] Review del PR #7 (María o Victor)
- [x] ~~Acceso al dashboard de Supabase~~ (resuelto el lunes)
- [ ] Nada más — todo bien 👍

---

## 💡 Aprendizajes / Notas

- pymavlink espera el heartbeat antes de poder recibir otros mensajes — esto no estaba documentado claramente, lo agregué al README
- La latencia de Supabase para upserts es ~80-120ms, bien dentro del budget de 1s
- Sugerencia: deberíamos agregar un health check endpoint al bridge para monitoreo

---

## 📊 Estado General

| Indicador | Estado |
|-----------|--------|
| **¿Estoy al día con el roadmap?** | 🟢 Sí |
| **¿Tengo bloqueos activos?** | 🟢 No |
| **¿Necesito ayuda?** | 🟢 No |
| **Confianza en la entrega de la fase** | 🟢 Alta |

---

*Template creado para el Proyecto Digital Twin GTI — Prácticas UDLAP 2026*
