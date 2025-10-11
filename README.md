# 📘 Lizcore Gym — Análisis y Preparación de Datos

## 🧠 Descripción general
Este proyecto forma parte de un análisis exploratorio de datos del gimnasio **Lizcore**, con el objetivo de **limpiar y estructurar la información** para posteriores análisis en **Power BI**. El foco estuvo en:
- Comprender la estructura del dataset original.
- Detectar y documentar nulos/duplicados.
- Diseñar un **pipeline reproducible de limpieza** con imputación por reglas.
- Generar un **dataset limpio** y un **resumen de popularidad de rutas** para su consumo en reporting.

---

## 📂 Estructura del repositorio

```
Lizcore_Gym/
│
├── data/
│   ├── lizcore_gym_data.csv                # Dataset original sin procesar
│   ├── lizcore_gym_data_clean.csv          # Dataset final limpio y enriquecido
│   └── route_popularity_summary.csv        # Resumen de popularidad de rutas
│
├── notebooks/
│   ├── 00.eda_preliminar.ipynb             # Exploración inicial (EDA) + chequeos rápidos
│   └── 01.limpieza.ipynb                   # Pipeline de limpieza, imputación y export
│
├── src/
│   └── sp_eda.py                           # Funciones reutilizables para EDA
│
└── README.md
```

---

## 🗂️ Descripción de datos de entrada
- **Filas/columnas:** 500 filas × 7 columnas.
- **Rango temporal:** del **2025-01-01** al **2025-03-01**.
- **Cobertura:** 100 usuarios únicos, 30 rutas distintas.
- **Nulos (dataset original):** `attempts` = 25 filas; `session_duration_min` = 26 filas.
- **Duplicados:** 0 (ninguno).
- **Posibles outliers de duración de sesión:** **5** casos detectados con la regla `< 40 min` o `> 140 min` (se marcan, no se eliminan).

---

## ⚙️ Pipeline de análisis (qué hice y por qué)

### 1) EDA preliminar (`00.eda_preliminar.ipynb` + `src/sp_eda.py`)
- Carga del CSV original y **vista aleatoria de registros** para validar contenido.
- **Chequeo estructural**: dimensiones, `df.info()`, tipos de datos.
- **Auditoría de calidad**:
  - Porcentaje de **nulos por columna**.
  - **Duplicados** a nivel de fila.
  - **Frecuencias** en columnas categóricas **sin truncar** (útil para detectar valores “casi iguales”, espacios, variantes).
- Todo esto se automatiza con la función **`eda_preliminar(df)`** en `sp_eda.py`, que imprime:
  - Muestra de 5 filas.
  - Dimensiones del dataset.
  - `info()` de tipos y memoria.
  - % de nulos por columna.
  - Conteos de categorías para todas las columnas `object` con limpieza de espacios.

### 2) Normalización y tipificación de campos (`01.limpieza.ipynb`)
- **Fecha**: se parsea `date` a tipo fecha para habilitar agregaciones temporales.
- **Grado (dificultad)**: se **ordena categóricamente** con la jerarquía:
  `5a < 5c < 6a < 6b < 6c < 7a < 7b`  
  Esto permite comparaciones y métricas coherentes por nivel.
- **Transparencia de imputaciones**: se crean **flags binarios**
  - `is_attempts_null` y `is_duration_null` para rastrear qué valores fueron imputados.
- **Outliers de duración**: se **etiquetan** (no se eliminan) con `is_duration_outlier` cuando `session_duration_min < 40` o `> 140` minutos.

### 3) Imputación dirigida por dominio
- Se calcula la **mediana por `grade`** para:
  - `attempts` → `attempts_imp`
  - `session_duration_min` → `session_duration_imp`
- La imputación se aplica **fila a fila** con la mediana de su **grado** (evitando sesgos globales).  
  > Decisión: mantener la **distribución por nivel** en lugar de rellenar con una única mediana global.

### 4) Enriquecimiento temporal (feature engineering)
Se derivan columnas de calendario a partir de `date`:
- `day`, `year`, `month_num`, `month_name`, `week_num`, `weekday_num`, `weekday_name`.  
Estas variables permiten analizar la **afluencia** por día/semana/mes y detectar patrones por **día de la semana**.

### 5) Métricas de control y “hechos” para reporting
- **Afluencia diaria** (`sessions_daily`) y **usuarios únicos por día** (`users_daily`) para checks de sanidad.
- **Éxito global** (`success_global`) como referencia de baseline.
- **Resumen de popularidad por ruta** → se agrupa por `route_id` y `grade` y se calcula:
  - `sessions` (n.º de sesiones),
  - `users` (n.º de usuarios únicos),
  - `success_rate` (tasa media de éxito),
  - `attempts_mean` (media de intentos imputados).  
  Resultado exportado a **`data/route_popularity_summary.csv`**.

### 6) Export de datasets
- **`lizcore_gym_data_clean.csv`**: dataset limpio con flags de calidad e imputaciones.  
  - Formato europeo: `sep=";"`, `decimal=","`, `float_format="%.2f"`.
- **`route_popularity_summary.csv`**: resumen ya agregado para visualizaciones.

---

## ✅ Qué queda en el dataset limpio (`data/lizcore_gym_data_clean.csv`)
Columnas principales (además de las originales):

- **Calidad / imputación**
  - `is_attempts_null`, `is_duration_null` → trazabilidad de celdas imputadas.
  - `attempts_imp`, `session_duration_imp` → valores finales usados en métricas.
  - `is_duration_outlier` → *flag* informativo, sin exclusión de registros.

- **Calendario**
  - `day`, `year`, `month_num`, `month_name`, `week_num`, `weekday_num`, `weekday_name`.

> Resultado: **0 nulos** en las columnas imputadas (`attempts_imp`, `session_duration_imp`) y control explícito del data lineage mediante flags.

---

## 📊 Indicadores y hallazgos (ejemplos)
- **Cobertura del dataset**: 500 registros entre **2025-01-01** y **2025-03-01**; 100 usuarios únicos y 30 rutas.
- **Calidad**: 25 nulos en `attempts` y 26 en `session_duration_min` se tratan con imputación **por grado**. No se eliminaron registros por outliers (solo **5** marcados).
- **Popularidad de rutas**: el archivo `route_popularity_summary.csv` recoge para cada ruta y grado: **n.º de sesiones, n.º de usuarios, tasa de éxito y media de intentos**; listo para ranking/filtrado en dashboards.

---

## 🧰 Stack tecnológico
- **Python 3** + **Jupyter Notebooks**
- **pandas, numpy** (transformación y agregados)
- **matplotlib** (visualización exploratoria)
- **Buenas prácticas de export**: CSV con separador `;` y coma decimal `,` para compatibilidad regional.

---

## 🚀 Próximos pasos
- Añadir **pruebas de calidad** (validaciones automáticas) previas al export.
- Promover el pipeline a un script/ETL **reproducible** con parámetros (input/output).
- Añadir una **dimensión fecha** persistida para análisis temporal completos.
- Integrar reglas de **detección avanzada de outliers** (IQR/z-score) y monitorizarlas.
- Orquestar el proceso (ej. `make`, `prefect`, `airflow`) y documentar dependencias.

---

## 📎 Notas de reproducibilidad
1. Ejecutar primero `00.eda_preliminar.ipynb` para validar estructuras.
2. Ejecutar `01.limpieza.ipynb` para generar:
   - `data/lizcore_gym_data_clean.csv`
   - `data/route_popularity_summary.csv`
3. Ver/editar funciones en `src/sp_eda.py` para personalizar el EDA.
