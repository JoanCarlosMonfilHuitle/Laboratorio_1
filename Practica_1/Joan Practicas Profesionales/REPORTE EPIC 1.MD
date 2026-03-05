# Sprint Report Semanal

**Proyecto:** GTI Digital Twin — Visualización de Drones  
**Periodo:** 24 de febrero – 28 de febrero  
**Fase:** Telemetry Foundation  
**Área:** Backend & Robotics  
**Practicante:** Joan Carlos Monfil Huitle

---

# Información

| Campo | Valor |
|------|------|
| Proyecto | GTI Digital Twin — Visualización de Drones |
| Semana | #4 (24 al 28 de febrero) |
| Fase | Telemetry Foundation |
| Practicante | Joan Carlos Monfil Huitle |
| Área | Backend & Robotics |

---

# Resumen Ejecutivo

Durante este sprint se logró la **integración funcional entre el backend de telemetría y el frontend de visualización del Digital Twin**.

El trabajo se centró en validar el funcionamiento completo del sistema conectando los componentes que previamente se habían desarrollado de manera independiente.

En términos generales se logró:

- Consolidar el **pipeline completo desde el simulador (SITL) hasta la visualización en el mapa**.
- Validar la **correcta ingesta de datos en Supabase**.
- Confirmar el **consumo de datos desde el frontend**.
- Visualizar en tiempo real la **posición actual del dron en el mapa**.
- Confirmar el funcionamiento **end-to-end del sistema**.

Este sprint representó un avance importante al conectar oficialmente el backend con el frontend y dejar preparada la base del sistema para futuras mejoras.

---

# Arquitectura del sistema

El flujo general del sistema validado durante este sprint se puede representar de la siguiente manera:


Simulador (SITL)
      ↓
MAVLink Telemetry
      ↓
Telemetry Bridge (Python + pymavlink)
      ↓
Supabase (Base de datos)
      ↓
Frontend Digital Twin
      ↓
Visualización en mapa en tiempo real

Este pipeline permite capturar datos de telemetría del dron y mostrarlos dentro de la interfaz del Digital Twin.

---

# Lo que hice esta semana

Durante este sprint se realizaron diversas actividades enfocadas en la integración del backend con el frontend y la validación del flujo de telemetría del sistema.

Actividades realizadas:

- Implementación de la conexión entre backend y frontend.
- Pruebas individuales de cada módulo.
- Integración progresiva de ambos sistemas.
- Corrección de errores detectados durante la integración.
- Ajustes en variables y configuraciones compartidas entre backend y frontend.

Estas actividades permitieron validar que los datos generados por el simulador pueden ser capturados, almacenados y visualizados correctamente.

---

# Testing

Se realizaron diferentes pruebas y modificaciones a los códigos creados e implementados.

Principales pruebas realizadas:

- Reinicio completo del sistema desde cero (SITL + QGroundControl + Bridge).
- Verificación de generación automática de `run_id`.
- Reinicio del frontend para validar actualización dinámica.
- Validación de actualización en tiempo real en Supabase.
- Confirmación de sincronización entre backend y frontend.
- Pruebas de detención limpia del sistema mediante `Ctrl + C`.

Estas pruebas permitieron confirmar el funcionamiento correcto del pipeline completo del sistema.

---

# Documentación y recursos utilizados

Durante el desarrollo del sprint también se revisaron recursos técnicos y documentación relacionada con la arquitectura del sistema.

Repositorio con documentación del backend:

https://github.com/vimaguelo/gti-satelites/tree/docs/backend-robotics-architecture/docs/digital-twin-backend-robotics

Video de referencia utilizado durante el desarrollo:

https://youtu.be/eT7p0d48PO0

---

# PRs creados / mergeados

PR: Códigos creados y modificados para integración con frontend  
Estado: En revisión / operativo

---

# Horas aproximadas trabajadas

22 horas

---

# Lo que haré la próxima semana

Durante el siguiente sprint se planea continuar con el desarrollo del proyecto y mejorar la organización del repositorio.

Actividades planeadas:

- Realizar pruebas adicionales de integración Backend/Robotics.
- Apoyar en Story 1.4 para aclarar dudas sobre backend y frontend.
- Continuar familiarizándome con herramientas del proyecto:

MAVLink  
SITL  
QGroundControl  
WSL  
Supabase  
Antigravity  
GitHub  

También se planea actualizar algunas carpetas del repositorio agregando imágenes del sistema en ejecución.

Estas imágenes aún no se han subido debido a que primero se espera obtener la aprobación del branch actual. Una vez validado el branch, se subirán imágenes que muestran los resultados obtenidos durante las pruebas.

---

# Bloqueos / Impedimentos

| Bloqueo | Impacto | Necesito |
|--------|--------|--------|
| Problemas con algunas aplicaciones y desfases de información | Entorpeció algunas tareas | Analizar mejor el trabajo realizado |
| Errores de código | Retrasos en integración | Revisar configuraciones entre módulos |

---

# Lo que necesito

- Revisar tabla `drone_telemetry`.
- Verificar el Telemetry Bridge (Python + pymavlink).
- Entender mejor el funcionamiento del frontend.
- Mejorar el manejo de GitHub respecto a branches.
- Revisar variables entre backend y frontend para evitar conflictos.

---

# Aprendizajes / Notas

Durante este sprint se obtuvieron varios aprendizajes importantes.

- Las tareas pueden tomar más tiempo del esperado, especialmente durante la integración de sistemas.
- Comprender los puentes de comunicación entre módulos es fundamental.
- Es útil entender el trabajo del resto del equipo para comprender el sistema completo.
- Es importante considerar los errores y el tiempo invertido en resolverlos.

También se observó que cuando se está concentrado resolviendo problemas técnicos, el tiempo puede pasar muy rápido sin que se perciba.

---

# Estado General

| Indicador | Estado |
|--------|--------|
| ¿Estoy al día con el roadmap? | 🟢 Sí |
| ¿Tengo bloqueos activos? | 🟡 Sí |
| ¿Necesito ayuda? | 🟡 Sí |
| Confianza en la entrega de la fase | 🟢 Alta |

---

Template creado para el Proyecto Digital Twin GTI — Prácticas UDLAP 2026

