# AI-Based-Kidney-Disease-Stage-Prediction

This project focuses on predicting **Chronic Kidney Disease (CKD)** and determining its **disease stage** using machine learning techniques. The model is trained on clinical data and enhanced with **eGFR (estimated Glomerular Filtration Rate)** calculation to accurately classify CKD stages.

---

## Project Overview

Chronic Kidney Disease (CKD) is a long-term condition where the kidneys gradually lose their ability to function properly. Early detection and accurate staging are essential for effective treatment and management.

This project aims to:

- Preprocess medical data related to kidney health  
- Calculate eGFR (estimated Glomerular Filtration Rate) using standard clinical formulas  
- Predict the presence of Chronic Kidney Disease using a machine learning model  
- Determine the stage of CKD based on calculated eGFR values

## Machine Learning Approach

- **Algorithm Used**: Random Forest Classifier (scikit-learn)  
- **Task Type**: Classification  
- **Target Variable**: CKD / Not CKD  

## Evaluation Metrics
- Accuracy Score  
- Classification Report (Precision, Recall, F1-score)

## eGFR Calculation

The eGFR value is calculated using the **MDRD equation**:

eGFR = 175 × (Serum Creatinine)^-1.154 × (Age)^-0.203

- Gender-based adjustment is applied where required eGFR is used to determine CKD stages  

### CKD Stages

| eGFR Value | CKD Stage |
|-----------|-----------|
| ≥ 90 | Stage 1 (Normal) |
| 60–89 | Stage 2 (Mild) |
| 30–59 | Stage 3 (Moderate) |
| 15–29 | Stage 4 (Severe) |
| < 15 | Stage 5 (Kidney Failure) |

---

##  Dataset

File: `kidney_disease.csv`  
Source: Public CKD dataset  

### Features Include
- Blood pressure  
- Serum creatinine  
- Hemoglobin  
- Albumin  
- Sugar  
- Red blood cells  
- Hypertension, Diabetes, Appetite, etc.  
- Categorical values are encoded numerically during preprocessing  

---

## Libraries & Tools Used

- Python 3.x  
- Pandas  
- NumPy  
- Scikit-learn  
- Jupyter Notebook  

---

##  Output

- Model accuracy score  
- Detailed classification report  
- Predicted CKD status  
- CKD stage based on calculated eGFR  

---

## Future Enhancements

- Use advanced models (Random Forest, XGBoost)  
- Add web interface using Flask  
- Improve accuracy with feature selection  
- Deploy model as a healthcare support system 
