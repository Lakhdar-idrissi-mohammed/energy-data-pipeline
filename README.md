# Energy Consumption Data Pipeline

## 📌 Project Overview
This project is an automated ETL (Extract, Transform, Load) pipeline designed to process raw energy meter data. It identifies data quality issues (duplicates, missing values), cleans the dataset using Python, and prepares it for visualization in Power BI.

## 🛠️ Tech Stack
* **Python (Pandas):** For data ingestion and cleaning (handling nulls/duplicates).
* **Matplotlib:** For automated trend analysis and static charting.
* **Power BI:** For interactive dashboarding.
* **Azure Context:** Designed to simulate an Azure Function processing logic.

## ⚙️ How It Works
1.  **Ingest:** script reads raw `meter_data.csv`.
2.  **Process:**
    * Converts timestamps to standard datetime objects.
    * Removes duplicate meter readings.
    * Imputes missing consumption values using a moving average strategy.
3.  **Output:** Generates `cleaned_data.csv` for reporting tools.

## 📊 Results
The pipeline successfully normalized the dataset, ensuring 100% data continuity for forecasting models.