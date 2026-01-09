# 📘 Lizcore Gym — Data Analysis & Preparation

## 🧠 Project Overview
This project is part of an **exploratory data analysis (EDA)** of the Lizcore climbing gym, with the objective of **cleaning, structuring, and preparing the data** for analytical use and visualization in **Power BI**.

The project focuses on:
- Understanding the structure and quality of the raw dataset.
- Detecting missing values, inconsistencies, and outliers.
- Designing a **reproducible data-cleaning pipeline**.
- Producing clean, analysis-ready datasets and aggregated metrics to support decision-making.

---

## 📂 Repository Structure

LIZCORE_GYMS/
│
├── data/
│ ├── lizcore_gym_data.csv # Raw dataset
│ ├── lizcore_gym_data_clean.csv # Cleaned and enriched dataset
│ └── route_popularity_summary.csv # Aggregated route popularity metrics
│
├── notebooks/
│ ├── 00.eda_preliminar.ipynb # Initial exploratory data analysis
│ └── 01.limpieza.ipynb # Data cleaning and transformation pipeline
│
├── src/
│ └── sp_eda.py # Reusable EDA helper functions
│
└── README.md


---

## 🗂️ Data Description
The original dataset contains session-level information from a climbing gym, including:
- User activity and route attempts
- Route difficulty (grade)
- Session duration and success
- Temporal information (date)

The dataset presents minor data quality issues such as missing values and extreme session durations, making it suitable for demonstrating a structured EDA and cleaning workflow.

---

## ⚙️ Data Analysis Pipeline

### 1. Preliminary Exploratory Data Analysis
**Files:** `00.eda_preliminar.ipynb`, `src/sp_eda.py`

The first step consisted of a structured EDA to assess data quality and structure:
- Random sampling of records to validate content.
- Inspection of dataset dimensions and data types.
- Quantification of missing values and duplicate records.
- Frequency analysis of categorical variables to detect inconsistencies.

To standardize this process, a reusable function `eda_preliminar(df)` was implemented, enabling fast and repeatable initial diagnostics across datasets.

---

### 2. Data Cleaning and Normalization
**File:** `01.limpieza.ipynb`

Key transformations included:
- Conversion of date fields to proper datetime formats.
- Definition of an **ordered categorical variable** for climbing grades:

- Creation of **data quality flags** to explicitly track imputed values:
- `is_attempts_null`
- `is_duration_null`

These flags ensure transparency and traceability throughout the pipeline.

---

### 3. Domain-Driven Imputation Strategy
Approximately **5% of sessions** were missing duration or attempt values.  
Rather than applying global statistics, missing values were imputed using a **conservative median-by-grade approach**, preserving performance differences across difficulty levels.

Extreme session durations (<40 min or >140 min) were **flagged as outliers but retained**, preventing unnecessary data loss.

---

### 4. Temporal Feature Engineering
To enable time-based analysis, several calendar features were derived:
- Year, month, week number
- Day of the week (numeric and label)

These features support downstream analyses such as attendance patterns and peak usage periods.

---

### 5. Analytical Outputs
Two main outputs were generated:
- **`lizcore_gym_data_clean.csv`**  
- Clean dataset with no missing values in key metrics.
- Explicit data-quality flags and imputed fields.
- Enriched temporal attributes.

- **`route_popularity_summary.csv`**  
- Aggregated metrics by route and grade:
  - Number of sessions
  - Number of unique users
  - Success rate
  - Average number of attempts  
- Designed for direct consumption in BI tools.

---

## 📊 Power BI — Key Insights

### Executive Summary
The analysis reveals **stable and predictable usage patterns**, with **higher occupancy on weekends** and lower attendance early in the week. Overall difficulty appears well balanced, with a **global success rate of approximately 51%**, indicating an effective mix of challenge and accessibility.

The **6c grade** stands out as both the most climbed and most successfully completed, representing an optimal engagement point. In contrast, grades **5a and 7a** show lower-than-expected success rates, suggesting these routes may be slightly harder than their nominal grading.

Activity is highly concentrated: the **top 10 most popular routes account for over 42% of total sessions**. At the same time, several routes show low recent activity, identifying them as candidates for **rotation or reset** to improve wall utilization and climber motivation.

From a data-quality perspective, missing values were handled using a **transparent, median-based imputation strategy**, while extreme sessions were preserved and flagged to retain analytical flexibility.

Overall, the project demonstrates how data analysis can **support operational planning**, **route-setting decisions**, and **staff allocation**, ultimately improving both efficiency and user experience.

---

## 🧰 Technology Stack
- **Language:** Python 3  
- **Environment:** Jupyter Notebook  
- **Libraries:**  
- pandas, numpy — data manipulation and analysis  
- matplotlib, seaborn — exploratory visualization  
- **Visualization:** Power BI

---

## 🚀 Next Steps
- Introduce automated data-quality validation checks.
- Convert the notebook workflow into a parameterized ETL script.
- Apply advanced outlier detection techniques.
- Expand behavioral analysis at the user level.
- Integrate orchestration for scheduled data processing.

---

## 📌 Notes
This project was designed with a **portfolio-oriented approach**, emphasizing clarity, reproducibility, and business-relevant insights rather than purely academic analysis.

