# Company Default Prediction using Machine Learning

This repository contains a machine learning project focused on predicting company defaults. The project utilizes various data preprocessing techniques, feature selection methods, and machine learning models to achieve high prediction accuracy. A user-friendly web interface is provided using Streamlit.

## Project Overview

Predicting company defaults is a crucial task for financial institutions and investors. This project aims to build a robust predictive model that can accurately identify companies at risk of defaulting. The project encompasses the following key steps:

*   **Data Preprocessing:** Cleaning and preparing the dataset for model training.
*   **Feature Engineering/Selection:** Identifying the most relevant features for prediction.
*   **Model Training and Evaluation:** Training and evaluating machine learning models.
*   **Web Application Development:** Creating an interactive web interface for easy use.

## Technologies Used

*   **Python:** Programming language.
*   **Scikit-learn:** Machine learning library.
*   **Pandas:** Data manipulation and analysis library.
*   **NumPy:** Numerical computing library.
*   **Imblearn:** Handling imbalanced datasets.
*   **Streamlit:** Web application framework.

## Data Preprocessing

The data preprocessing steps included:

*   **Missing Value Handling:** Identification and imputation of missing values using the KNN imputer.
*   **Outlier Treatment:** Detection and handling of outliers to improve model robustness.
*   **Feature Scaling:** Scaling numerical features to a standard range using appropriate methods (e.g., StandardScaler, MinMaxScaler).
*   **Imbalance Treatment:** Addressing class imbalance using techniques like oversampling (e.g., SMOTE) or undersampling.

## Feature Selection

Feature selection methods used:

*   **ANOVA (Analysis of Variance):** Statistical test to assess the significance of features.
*   **Correlation Analysis:** Identifying and removing highly correlated features.

## Models Used

The following machine learning models were trained and evaluated:

*   **RandomForest Classifier:** Ensemble learning method known for its robustness and accuracy.
*   **XGBoost Classifier:** Gradient boosting algorithm that often achieves state-of-the-art performance.

## Results

The models achieved an accuracy of over 98% on the test dataset. Further metrics like precision, recall, F1-score, and AUC-ROC were also considered for a comprehensive evaluation.
