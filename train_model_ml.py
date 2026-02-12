import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib
import os

print("Loading dataset...")
import os
import gdown  # pip install gdown
import pandas as pd

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Path to dataset
dataset_path = "data/creditcard.csv"

# Download dataset if it doesn't exist
if not os.path.exists(dataset_path):
    url = "https://drive.google.com/uc?id=YOUR_FILE_ID"  # replace with your file's ID
    gdown.download(url, dataset_path, quiet=False)

# Now load the dataset
data = pd.read_csv(dataset_path)

# Rest of your training code below

# Load dataset
df = pd.read_csv("data/creditcard.csv")

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------
# Check class distribution
# -----------------------------
print("\nClass Distribution:")
print(df['Class'].value_counts())

# -----------------------------
# Preprocessing
# -----------------------------

# Scale Amount
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
df.drop(['Amount'], axis=1, inplace=True)

# Features & Target
X = df.drop('Class', axis=1)
y = df['Class']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nData split completed")

# -----------------------------
# Handle Imbalance (SMOTE)
# -----------------------------
print("\nApplying SMOTE to balance dataset...")

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

print("After SMOTE:")
print(pd.Series(y_train_resampled).value_counts())

# -----------------------------
# Model 1: Logistic Regression
# -----------------------------
print("\nTraining Logistic Regression...")

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train_resampled, y_train_resampled)

# -----------------------------
# Model 2: Random Forest
# -----------------------------
print("\nTraining Random Forest...")

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_resampled, y_train_resampled)

# -----------------------------
# Predictions
# -----------------------------
y_pred_lr = lr.predict(X_test)
y_pred_rf = rf.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
print("\n========== Logistic Regression Results ==========")
print(classification_report(y_test, y_pred_lr))

print("\nConfusion Matrix (LR):")
print(confusion_matrix(y_test, y_pred_lr))

print("\n========== Random Forest Results ==========")
print(classification_report(y_test, y_pred_rf))

print("\nConfusion Matrix (RF):")
print(confusion_matrix(y_test, y_pred_rf))

# -----------------------------
# Save Best Model (Random Forest)
# -----------------------------
os.makedirs("model", exist_ok=True)
joblib.dump(rf, "model/fraud_model.pkl")

print("\nModel saved as model/fraud_model.pkl")
print("TRAINING COMPLETED SUCCESSFULLY")
