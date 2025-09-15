# Lizcore Gyms — Data & BI Project

Proyecto de analítica para **Lizcore** orientado a:
1) EDA y limpieza en **Python**  
2) Modelado de KPIs y visualización en **Power BI**

> Objetivo: entender uso de gyms, retención/churn, revenue y performance de clases/usuarios para proponer acciones.

---

## 🚀 Estructura recomendada
```
lizcore_gyms/
├─ data/
│  ├─ raw/            # datos originales (no tocar)
│  ├─ interim/        # salidas intermedias
│  └─ processed/      # datasets limpios para BI
├─ notebooks/         # exploración/EDA
├─ src/               # scripts reutilizables
│  ├─ etl/            # extracción/transformaciones
│  └─ features/       # ingeniería de variables
├─ reports/
│  └─ figures/        # gráficos exportados
├─ powerbi/           # archivos .pbix/.pbit (usar LFS si se versionan)
├─ tests/             # pruebas unitarias (opcional)
├─ requirements.txt
└─ README.md
```

> Crea `.gitkeep` vacíos en carpetas vacías para versionarlas.

---

## 🧰 Requisitos
- Python 3.10+
- Power BI Desktop
- (Opcional) **Git LFS** si vas a versionar `.pbix/.pbit`

Instalación de entorno:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Sugerencia de `requirements.txt` mínimo:
```
pandas
numpy
matplotlib
scikit-learn
pyarrow
python-dotenv
```

---

## 📓 Flujo de trabajo

### 1) EDA & limpieza (Python)
- `notebooks/01_eda.ipynb`: exploración inicial, nulos, outliers, duplicados.
- `src/etl/cleaning.py`: funciones para estandarizar categorías, fechas, ids.
- `src/features/feature_build.py`: flags de **churn**, recencia, frecuencia, monetización (RFM), engagement, etc.
- **Salida:** `data/processed/fact_*.parquet` y `dim_*.parquet` listos para BI.

### 2) Modelado para BI
- Define **tablas**: `fact_subscriptions`, `fact_visits`, `fact_sales`, `dim_user`, `dim_gym`, `dim_date`.
- Reglas de negocio documentadas en `docs/metrics.md`:
  - **Churn**: usuario dado de baja o >X días sin visita/renovación (definición acordada con negocio).
  - **Retención**: 1 - churn.
  - **ARPU**, **MRR**, **LTV**.

### 3) Power BI
- Importa desde `data/processed/` (parquet/csv).
- Modela relaciones (star schema).
- Métricas DAX recomendadas:
  - `Churn Rate`, `Retention Cohorts`, `Active Users (MAU/WAU/DAU)`,
  - `Revenue`, `ARPU`, `MRR`, `LTV`, `Conversion Funnel`.

---

## 🗂️ Datos esperados (ejemplo)
- **users.csv**: `user_id`, `signup_date`, `plan`, `status`, etc.
- **visits.csv**: `visit_id`, `user_id`, `gym_id`, `checkin_ts`, `activity_type`.
- **subscriptions.csv**: `user_id`, `start`, `end`, `price`, `renewal`.
- **sales.csv**: `sale_id`, `user_id`, `item`, `amount`, `ts`.

Cada dataset puede incluir **nulos** y **inconsistencias** para simular casos reales.

---

## ✅ Checklists rápidos

### Pre-EDA
- [ ] Validar esquema y tipos
- [ ] Inventario de nulos y duplicados
- [ ] Reglas de negocio acordadas

### Pre-Power BI
- [ ] Tablas `fact` y `dim` separadas
- [ ] Claves y granularidad definidas
- [ ] Diccionario de datos actualizado

---

## 🔁 Git — flujo sugerido
```bash
git checkout -b feature/eda
# ... trabajo ...
git commit -m "EDA inicial + limpieza base"
git push -u origin feature/eda
# PR a main
```

Si versionas `.pbix/.pbit` añade LFS:
```bash
git lfs install
git lfs track "*.pbix" "*.pbit"
git add .gitattributes
git commit -m "Track PBIX with LFS"
```

---

## 📄 Licencia
Uso interno para propuesta de portafolio y demo para Lizcore.
