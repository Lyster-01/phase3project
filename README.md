# phase3project
## 🔍 Business Understanding
Cancer remains one of the leading causes of death globally, with its complexity and variability making treatment and prediction challenging. Health institutions are increasingly relying on data-driven approaches to improve patient outcomes. Accurate prediction of patient severity and survival likelihood can help healthcare providers prioritize care, allocate resources more effectively, and tailor treatment plans for better patient outcomes.

This project seeks to apply data science methods to a synthetic global cancer patient dataset spanning from 2015 to 2024. The key goal is to explore and predict patient health outcomes based on demographic, lifestyle, and clinical variables using both statistical and machine learning techniques.

## 🧠 Data Understanding
The dataset titled Global Cancer Patients 2015–2024 is a synthetic representation of cancer patient records from multiple countries. Each record includes personal demographics, environmental and lifestyle risk factors, treatment costs, cancer type and stage, survival duration, and a calculated severity score. Although synthetic, the dataset is designed to mimic real-world patterns and can be used for educational, analytical, and modeling purposes.
### 📋 Feature Descriptions:
Feature	Description
Patient_ID	Unique identifier for each patient
Age	Age of the patient in years
Gender	Gender of the patient (Male/Female)
Country_Region	Geographic location of the patient
Year	Year of diagnosis
Genetic_Risk	Scaled score (0–10) reflecting genetic predisposition to cancer
Air_Pollution	Level of environmental pollution exposure (0–10 scale)
Alcohol_Use	Level of alcohol consumption (0–10 scale)
Smoking	Level of tobacco use (0–10 scale)
Obesity_Level	Obesity score (0–10 scale)
Cancer_Type	Type of cancer diagnosed
Cancer_Stage	Stage of cancer (Stage 0 to Stage IV)
Treatment_Cost_USD	Cost of treatment in USD
Survival_Years	Number of years the patient survived after diagnosis
Target_Severity_Score	A derived severity score (0–10) representing clinical severity

## 📌 Problem Statement
The healthcare industry constantly seeks innovative solutions to optimize cancer care delivery and reduce mortality rates. Leveraging data science to analyze cancer-related data can provide actionable insights into patient outcomes and treatment planning.

This project aims to analyze and model cancer patient data to:

1. To compute and visualize the correlation between the Target Severity Score and continuous risk factors.
2. To investigate whether survival outcomes differ significantly across various cancer stages.
3. To predict whether a patient has a high severity score.
4. To predict whether a patient will survive more than 5 years after diagnosis.
---------

Understand the relationships between risk factors and severity.

Test whether cancer stage significantly affects survival.

Build predictive models to anticipate high-severity cases.

Predict which patients are likely to survive beyond five years.

By achieving these objectives, healthcare professionals can gain decision-support tools that aid in early interventions and effective resource allocation.

