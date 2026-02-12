//TITLE

Credit Card Fraud Detection Using Machine Learning

//INTRODUCTION

This project focuses on detecting fraudulent credit card transactions using machine learning techniques. Financial fraud causes significant losses to banks and customers every year, and manual detection is slow and inefficient. The proposed system analyzes transaction data and automatically classifies whether a transaction is legitimate or fraudulent. By training models such as Logistic Regression, Random Forest, and XGBoost on historical transaction data, the system aims to identify suspicious patterns and improve fraud detection accuracy while minimizing false alarms.

//PROBLEM STATEMENT

Banks process millions of transactions daily.
Only a very small percentage are fraud → this creates a class imbalance problem.
Challenges:
- Fraud transactions are rare
- Hard to detect manually
- Normal transactions look similar to fraud
- Delayed detection leads to financial loss
Goal:
Build a machine learning model that detects fraud transactions quickly and accurately with high recall and low false positives.

//DATASET

Source: Public credit card transaction dataset(KAGGLE)
- Contains anonymized transaction features
- Includes transaction amount and class label
- Class = 0 → Legitimate
- Class = 1 → Fraud
-The dataset is highly imbalanced.

//TECHNOLOGIES USED

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook / VS Code

//METHODOLOGY/WORKFLOW

1. Data loading
2. Data preprocessing
3. Handling missing values
4. Exploratory Data Analysis (EDA)
5. Handling class imbalance (SMOTE / undersampling)
6. Feature scaling (StandardScaler)
7. Model training
8. Model evaluation
9. Performance comparison

//MACHINE LEARNING MODELS USED

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

//EVALUATION METRICS

Because fraud dataset is imbalanced, accuracy alone is misleading.
So we used:
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

//FEATURES OF THE SYSTEM 

1. Automatic fraud detection
2. Works on large datasets
3. Identifies suspicious patterns
4. Reduces manual effort
5. Improves financial security

//APPLICATIONS

1. Banking systems
2. Online payments
3. E-commerce platforms
4. Digital wallets

//FUTURE SCOPE

- Real-time fraud detection API
- Deep learning models
- Integration with banking software
- Mobile alert system for customers