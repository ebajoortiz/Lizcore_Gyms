📘 Lizcore Gym — Data Analysis & Preparation
🧠 Project Overview

This project is part of an exploratory data analysis of the Lizcore gym, with the objective of cleaning, structuring, and preparing the data for subsequent analysis and visualization in Power BI.

The main focus of the project was to:

Understand the structure and quality of the raw dataset.

Detect and document missing values and potential anomalies.

Build a reproducible data-cleaning pipeline.

Generate clean, analysis-ready datasets suitable for reporting and dashboarding.

📂 Repository Structure
LIZCORE_GYMS/
│
├── data/
│   ├── lizcore_gym_data.csv                # Raw dataset
│   ├── lizcore_gym_data_clean.csv          # Cleaned and enriched dataset
│   └── route_popularity_summary.csv        # Aggregated route popularity metrics
│
├── notebooks/
│   ├── 00.eda_preliminar.ipynb             # Initial exploratory data analysis
│   └── 01.limpieza.ipynb                   # Data cleaning and transformation pipeline
│
├── src/
│   └── sp_eda.py                           # Reusable EDA helper functions
│
└── README.md

🗂️ Input Data Description

The original dataset contains information about gym sessions, routes, and user performance.

Key characteristics:

Multiple users and climbing routes across different difficulty grades.

Session-level information including attempts, duration, success, and date.

Presence of missing values in numeric columns and the need for consistent typing.

This dataset serves as the base for all subsequent transformations and analysis.

⚙️ Analysis & Data Pipeline (Step by Step)
1. Preliminary Exploratory Data Analysis

Files: 00.eda_preliminar.ipynb, src/sp_eda.py

The first step was to perform a structured exploratory analysis to assess data quality and structure:

Random sampling of records to validate content.

Inspection of dataset dimensions and data types (df.info()).

Quantification of missing values by column.

Duplicate detection.

Frequency analysis of categorical variables to identify inconsistencies (extra spaces, variants, unexpected categories).

To streamline this process, a reusable function called eda_preliminar(df) was implemented in sp_eda.py.
This function standardizes the initial EDA process and can be reused across datasets.

2. Data Normalization and Typing

File: 01.limpieza.ipynb

Key transformations applied:

Conversion of the date column to a proper datetime format.

Definition of an ordered categorical variable for route difficulty (grade), ensuring logical comparisons:

5a < 5c < 6a < 6b < 6c < 7a < 7b


Creation of explicit data quality flags:

is_attempts_null

is_duration_null
These flags preserve traceability of imputed values.

3. Domain-Driven Missing Value Imputation

Instead of using global statistics, missing values were imputed using median values by difficulty grade:

attempts_imp

session_duration_imp

This approach preserves performance differences across climbing levels and avoids bias introduced by global aggregates.

Potential duration outliers were flagged but not removed, allowing downstream analyses to decide how to handle them.

4. Temporal Feature Engineering

To support time-based analysis and reporting, several calendar features were derived from the date field:

Day, month, year

Week number

Day of week (numeric and label)

These features enable analyses such as session frequency by weekday or seasonal trends.

5. Aggregated Metrics and Analytical Outputs

Several derived datasets and metrics were created to support reporting use cases:

Daily session counts and unique user counts (sanity checks).

Global success-rate baseline.

Route popularity summary, aggregated by route and grade:

Number of sessions

Number of unique users

Average success rate

Mean number of attempts

This aggregation is exported as route_popularity_summary.csv.

6. Final Outputs

The pipeline generates two main outputs:

lizcore_gym_data_clean.csv
A clean, analysis-ready dataset with:

No missing values in key numeric fields.

Quality flags and imputed columns clearly separated.

Enriched temporal features.

route_popularity_summary.csv
A compact, aggregated dataset ready for visualization and ranking.

📊 Key Outcomes

The analysis of Lizcore gym data reveals stable and predictable usage patterns, with higher occupancy on weekends and lower attendance at the beginning of the week. Overall activity shows a balanced difficulty level, with a global success rate of approximately 51%, indicating a good balance between challenge and accessibility.

From a difficulty perspective, grade 6c stands out as both the most climbed and most successfully completed, representing an optimal engagement point. In contrast, grades such as 5a and 7a show lower-than-expected success rates, suggesting that these routes may be slightly harder than their nominal grade.

Route popularity analysis highlights a strong concentration of activity, as the top 10 routes account for over 42% of total sessions. At the same time, several routes show low recent activity, identifying them as candidates for rotation or reset to improve wall utilization and climber motivation.

From a data quality standpoint, a small proportion of sessions lacked recorded duration or attempts (≈5%). These cases were handled using a conservative median-based imputation by grade, while extreme session durations were retained and flagged as outliers to preserve information.

Overall, this project demonstrates how data analysis can support operational, route-setting, and staffing decisions, ultimately improving both efficiency and user experience in a climbing gym.

🧰 Technology Stack

Language: Python 3

Environment: Jupyter Notebooks

Libraries:

pandas, numpy — data manipulation and analysis

matplotlib, seaborn — exploratory visualization

Downstream tools: Power BI (dashboarding and reporting)

🚀 Next Steps

Introduce automated data-quality validation checks.

Convert the notebook pipeline into a parameterized ETL script.

Enhance outlier detection using statistical methods (IQR, z-score).

Integrate orchestration and scheduling.

Expand temporal and behavioral analyses at user level.
