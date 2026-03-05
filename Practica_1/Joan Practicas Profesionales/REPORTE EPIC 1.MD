# Reporte General — Sprint Semana 4  
**GTI Digital Twin (Backend/Robotics + Frontend)**  
**Horas invertidas:** 22

---

## Resumen para “Informe de Sprint” (Semana 4)

### ¿Qué se completó?
- Se integró el flujo de telemetría del backend con la visualización del frontend para mostrar la **posición del dron en el mapa**.
- Se consolidó y documentó el módulo Backend/Robotics: **arquitectura, flujo de telemetría, Supabase (schema, RLS, vistas y queries) y MAVLink**.
- Se incorporó el **script del Telemetry Bridge** en el repositorio para revisión del equipo y trazabilidad del pipeline (**MAVLink → Supabase**).
- Se trabajó en GitHub con buenas prácticas: **creación/organización de carpetas, commits, trabajo por branch** y actualización de documentación.
- Se validó el consumo de datos desde Supabase mediante vistas (**latest_snapshot** y **latest_snapshot_mapbox**) para uso en mapas.

### Enlaces (repo / PR / branch)
- Pega aquí el enlace al repositorio, PR, o branch donde se realizó la integración y la documentación.

---

## Plan para la próxima semana

### ¿En qué planeas trabajar?
- Refinar la integración Frontend–Backend (estabilidad del refresco en tiempo real, manejo de reconexión y validación de formatos para Mapbox).
- Agregar capturas y diagramas (carpeta `images/`) para evidenciar el flujo completo, y mejorar la documentación para onboarding.
- Definir/ajustar endpoints o vistas adicionales si el frontend requiere más atributos (altitud, heading, batería, etc.).
- Pruebas de consistencia y performance (frecuencia de inserción, lat/lon, `run_id` por sesión).

### Historias planificadas para la próxima semana
- Lista breve de historias/tareas del tablero (ej. “Mapa en tiempo real”, “Mejorar RLS”, “Documentación de onboarding”, etc.).

### Bloqueadores
- No (por ahora). Si aparece alguno: acceso/keys, permisos RLS, puertos MAVLink, o cambios de esquema.

### Autoevaluación
- Problemas menores (hubo ajustes finos de documentación/diagramas y orden del repo, pero el avance fue sostenido).

### Aprendizajes (opcional)
- Cómo estructurar documentación técnica en GitHub para que sea mantenible (carpetas, README, arquitectura, flujo).
- Cómo usar vistas en Supabase para simplificar el consumo del frontend (incluyendo conversión lat/lon a grados).
- Importancia de separar sesiones con `run_id` para depurar y no mezclar corridas del bridge.

---

## Reporte general (detallado pero general)

### Contexto y objetivo del sprint
Durante la Semana 4 se consolidó el avance del proyecto GTI Digital Twin enfocándose en la conexión práctica entre backend y frontend.  
El objetivo principal fue asegurar que la telemetría generada por el dron (o SITL) pudiera fluir de forma consistente desde MAVLink hacia Supabase, y que el frontend lograra consumir esos datos para visualizar la posición del dron en un mapa. Esto deja una base lista para extender la visualización con más variables (altitud, orientación, batería, etc.).

### Trabajo realizado (visión general)
- Backend/Robotics: se aseguró el pipeline **MAVLink → Telemetry Bridge → Supabase**, guardando snapshots periódicos para evitar saturación de datos.
- Supabase: se definió el **esquema** de la tabla `drone_telemetry` y se dejaron listas **políticas (RLS)** y **vistas** para consumo simple del frontend.
- Vistas/Queries: se documentó `latest_snapshot` para obtener el último estado y `latest_snapshot_mapbox` para convertir coordenadas a grados decimales.
- Repositorio/GitHub: se organizó la documentación del módulo en carpetas, se trabajó por branches y se dejaron commits como evidencia técnica.
- Frontend: se conectó el consumo de datos con la visualización del mapa, logrando mostrar la posición del dron en tiempo real a nivel funcional.

### Resultados y evidencia
El resultado principal del sprint es una integración funcional donde el frontend ya puede mostrar el mapa y la posición del dron usando datos persistidos en Supabase.  
Además, el repositorio quedó con documentación que permite a cualquier integrante entender rápidamente el flujo: arquitectura general, flujo de telemetría, bridge, Supabase (schema/RLS/vistas) y MAVLink (tipos de mensajes).

### Puntos clave (lo más importante)
- Se logró el “camino completo” de datos: generación → captura → almacenamiento → consumo en UI.
- Se habilitó depuración por sesión con `run_id` para separar corridas.
- Se estandarizó documentación del módulo para revisión y mantenimiento.
- Se preparó una base para crecer a más features (más atributos, filtros, históricos, performance).

### Riesgos / consideraciones
- Asegurar que las llaves/roles de Supabase se manejen de forma segura (service role key nunca en frontend).
- Mantener consistencia de unidades (lat/lon escalados, altitudes, velocidades) para evitar errores de interpretación.
- Controlar frecuencia de inserción para evitar crecimiento excesivo de datos y costos.
- Revisar que RLS permita lo necesario sin abrir acceso de más.

### Siguientes pasos recomendados
- Agregar evidencias visuales (capturas y diagramas) y enlazarlas desde los `.md` principales.
- Completar pruebas end-to-end (mover dron/SITL y validar lat/lon/heading/alt en UI).
- Agregar un set mínimo de métricas/alertas: batería baja, pérdida de heartbeat, reconexión MAVLink.
- Definir consultas de históricos por `run_id` y/o rango de tiempo para trazas en el frontend.
