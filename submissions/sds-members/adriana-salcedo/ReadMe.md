# Fraud Detection Modeling

This repository contains a Python implementation for fraud detection using a highly imbalanced dataset. The project demonstrates the end-to-end process from data preprocessing and feature engineering to model training, hyperparameter tuning, evaluation, and feature importance analysis using various machine learning algorithms.


## Overview

- **Original Dataset:**  
  The original dataset is available on Kaggle:  
  [Online Payment Fraud Detection Dataset](https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection)  
  A separate notebook was used to preprocess the raw data, resulting in the file `processed_data.csv` which is used for all modeling in this project.

- **Data Exploration and Feature Engineering:**  
  A dedicated notebook was created to analyze and preprocess the data. In that notebook, key characteristics of the dataset were examined, including:
  - **Dataset Structure:**  
    The dataset includes features such as:
    - `step` (time step in hours),
    - `type` (transaction type),
    - `amount` (transaction amount),
    - `nameOrig` (originating account),
    - `oldbalanceOrg` and `newbalanceOrig` (originator’s balances before and after the transaction),
    - `nameDest` (recipient account),
    - `oldbalanceDest` and `newbalanceDest` (recipient’s balances before and after the transaction),
    - `isFraud` (indicator of fraud), and 
    - `isFlaggedFraud` (fraud flag).
  
  - **Feature Engineering:**  
    Based on the initial exploratory data analysis, additional features were generated:
    - **Frequency Encoding:** Calculating the frequency of each destination account (`nameDest_freq`) to capture account activity levels.
    - **Fraud Rate Encoding:** Computing the fraud rate for each destination account (`nameDest_fraud_rate`) to assess associated risk.
  
  - **Preliminary Data Analysis:**  
    The EDA revealed a strong class imbalance, a right-skewed distribution of transaction amounts, and the presence of significant outliers—all of which influenced the modeling approach.

- **Preprocessing:**  
  The project uses a `ColumnTransformer` pipeline that:
  - Applies a logarithmic transformation followed by standard scaling to numerical features like `amount`, `oldbalanceOrig`, `newbalanceOrig`, etc.
  - Standard scales other numeric features.
  - One-hot encodes categorical features such as `type` and several binary indicator columns.
  
- **Modeling:**  
  Three models are built and evaluated:
  - **Logistic Regression**
  - **Random Forest**
  - **XGBoost**
  
  In each pipeline, after preprocessing, a simple random undersampling strategy (using `RandomUnderSampler`) is applied to the majority class to handle the imbalance. Due to capacity and runtime constraints, computationally intensive oversampling methods (e.g., SMOTE or SMOTEENN) were not used. While this undersampling approach greatly reduces processing time, it may lead to models that do not perform optimally on the minority class.

- **Hyperparameter Tuning and Evaluation:**  
  Hyperparameter tuning is conducted using Grid Search or Randomized Search along with cross-validation. Evaluation metrics include:
  - Classification Reports (with adjusted probability thresholds, e.g., 0.3),
  - Confusion Matrices,
  - ROC Curves,
  - Feature Importance plots.
  
  The models’ performance reflects the trade-off between faster computation (using undersampling) and potentially lower performance in detecting the minority class.

---

## Repository Structure

- **`model_implementation.py`**  
  The main script/notebook containing the modeling pipeline—from data loading and preprocessing to model training, hyperparameter tuning, evaluation, and saving of model configurations.

- **`data_preprocessing.py`**  
  A separate notebook for exploratory data analysis, initial preprocessing, and feature engineering on the raw Kaggle dataset. The output from this notebook is the `processed_data.csv` file.

- **`model_config/`**  
  A directory that stores saved models and corresponding parameter files (e.g., `lr_model.pkl`, `lr_best_params.json`, `rf_model.pkl`, etc.).

---

## Requirements

- Python 3.7+
- Required packages:
  - pandas
  - numpy
  - scikit-learn
  - imbalanced-learn
  - xgboost
  - joblib
  - matplotlib
  - seaborn
  - python-dotenv

To install the required packages, run:

```bash
pip install pandas numpy scikit-learn imbalanced-learn xgboost joblib matplotlib seaborn python-dotenv
``` 

## How to Run

1. **Data Preparation**:

    Run the data_preprocessing.py notebook to process the raw data and generate processed_data.csv.

2. **Model Training and Evaluation**:

    Execute the main script/notebook (modeling (4).py) using your preferred Python environment or IDE. The script loads the preprocessed data, applies preprocessing and feature engineering, trains the models, tunes hyperparameters, and evaluates model performance.

3. **Model Files and Parameters**:

    The best models and their tuned parameters are saved in the model_config directory (e.g., the Logistic Regression model is saved as lr_model.pkl with parameters in lr_best_params.json).

## Additional Notes
**Sampling Strategy**:

Due to capacity and runtime constraints, this project uses simple random undersampling (applied only on the majority class) instead of more computationally expensive oversampling techniques like SMOTE/SMOTEENN. This greatly reduces processing time but may lead to suboptimal detection of the minority class.

**Threshold Adjustment**:

Custom probability thresholds (e.g., 0.3 instead of the default 0.5) are used during model evaluation to enhance the recall for fraudulent cases.

**Performance Trade-offs**:

The modeling approach reflects a balance between faster processing and improved model performance. Future iterations may investigate advanced sampling or cost-sensitive methods to further enhance minority class detection.

**Feature Engineering Notebook**:

The separate EDA and feature engineering notebook provides detailed insights into the dataset’s structure, identifies key trends (such as skewness and outliers), and explains the rationale behind the engineered features. This information can be used to guide further improvements in both preprocessing and modeling.


## 🔍 Final Reflection & Limitations

Throughout this fraud detection project, I implemented and compared three classification models: Logistic Regression, Random Forest, and XGBoost. Each model was optimized with hyperparameter tuning and custom threshold selection based on the F1 score.

### Model Strengths & Strategy

- **Logistic Regression** provided transparent insights into feature influence through interpretable coefficients. It allowed effective threshold tuning on a 10% test sample.
  
- **Random Forest** offered strong performance and robustness. Thanks to `SelectFromModel` and adjusted thresholds, the model achieved a high F1 score (~0.68) and maintained a solid balance between precision and recall.

- **XGBoost** delivered fast and stable training, making it possible to evaluate on the full test set without subsampling. Its performance remained robust, especially with `scale_pos_weight` adjustment for class imbalance. Threshold optimization was directly performed on the full prediction set, avoiding sampling steps due to efficiency.

### Feature Engineering & Caution

- Features like `nameDest_fraud_rate` proved to be extremely powerful across all models. However, its strong predictive power can also pose a **risk of data leakage**, as it may incorporate information that wouldn’t be available in real-time scenarios. While it was retained for this version, this is clearly flagged in the code and should be revisited for production use.

- Feature selection with `SelectFromModel` helped reduce overfitting and improve model generalization. However, in cases where strong features dominate, they can overshadow less obvious patterns.

### 🔍 Final Reflection & Limitations

Throughout this fraud detection project, I implemented and compared three classification models: Logistic Regression, Random Forest, and XGBoost. Each model was optimized with hyperparameter tuning and custom threshold selection based on the F1 score.

### Model Strengths & Strategy

- **Logistic Regression** provided transparent insights into feature influence through interpretable coefficients. It allowed effective threshold tuning on a 10% test sample.
  
- **Random Forest** offered strong performance and robustness. Thanks to `SelectFromModel` and adjusted thresholds, the model achieved a high F1 score (~0.68) and maintained a solid balance between precision and recall.

- **XGBoost** delivered fast and stable training, making it possible to evaluate on the full test set without subsampling. Its performance remained robust, especially with `scale_pos_weight` adjustment for class imbalance. Threshold optimization was directly performed on the full prediction set, avoiding sampling steps due to efficiency.

### Feature Engineering & Caution

- Features like `nameDest_fraud_rate` proved to be extremely powerful across all models. However, its strong predictive power can also pose a **risk of data leakage**, as it may incorporate information that wouldn’t be available in real-time scenarios. While it was retained for this version, this is clearly flagged in the code and should be revisited for production use.

- Feature selection with `SelectFromModel` helped reduce overfitting and improve model generalization. However, in cases where strong features dominate, they can overshadow less obvious patterns.

## Final Reflection & Limitations

Throughout this fraud detection project, I implemented and compared three classification models: Logistic Regression, Random Forest, and XGBoost. Each model was optimized with hyperparameter tuning and custom threshold selection based on the F1 score.

### Model Strengths & Strategy

- **Logistic Regression** provided transparent insights into feature influence through interpretable coefficients. It allowed effective threshold tuning on a 10% test sample.
  
- **Random Forest** offered strong performance and robustness. Thanks to `SelectFromModel` and adjusted thresholds, the model achieved a high F1 score (~0.68) and maintained a solid balance between precision and recall.

- **XGBoost** delivered fast and stable training, making it possible to evaluate on the full test set without subsampling. Its performance remained robust, especially with `scale_pos_weight` adjustment for class imbalance. Threshold optimization was directly performed on the full prediction set, avoiding sampling steps due to efficiency.

### Feature Engineering & Caution

- Features like `nameDest_fraud_rate` proved to be extremely powerful across all models. However, its strong predictive power can also pose a **risk of data leakage**, as it may incorporate information that wouldn’t be available in real-time scenarios. While it was retained for this version, this is clearly flagged in the code and should be revisited for production use.

- Feature selection with `SelectFromModel` helped reduce overfitting and improve model generalization. However, in cases where strong features dominate, they can overshadow less obvious patterns.


## Live Demo

This project includes an interactive fraud detection app built with Gradio and deployed on Hugging Face Spaces.

 [💸 Try it live on Hugging Face](https://huggingface.co/spaces/Adriana213/fraud-predictor)

The app uses the final Random Forest model with a custom threshold and feature selection.

