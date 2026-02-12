import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler


print("Loading trained model...")

model = joblib.load("model/fraud_model.pkl")

print("Model Loaded Successfully")

# Load one sample transaction
df = pd.read_csv("data/creditcard.csv")
# Same preprocessing as training
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df[['Amount']])
df.drop('Amount', axis=1, inplace=True)

# ---------- NORMAL TRANSACTION ----------
print("\nChecking a NORMAL transaction...")
normal_row = df[df['Class'] == 0].iloc[0:1]
normal_sample = normal_row.drop('Class', axis=1)

normal_pred = model.predict(normal_sample)
normal_prob = model.predict_proba(normal_sample)

if normal_pred[0] == 0:
    print("Prediction: NORMAL TRANSACTION")
else:
    print("Prediction: FRAUD")

print("Fraud Probability:", normal_prob[0][1])


# ---------- FRAUD TRANSACTION ----------
print("\nChecking a FRAUD transaction...")
fraud_row = df[df['Class'] == 1].iloc[0:1]
fraud_sample = fraud_row.drop('Class', axis=1)

fraud_pred = model.predict(fraud_sample)
fraud_prob = model.predict_proba(fraud_sample)

# Set custom threshold (e.g., 0.2 for more sensitive fraud detection)
fraud_threshold = 0.2

if fraud_prob[0][1] >= fraud_threshold:
    print("Prediction: FRAUD TRANSACTION")
else:
    print("Prediction: NORMAL")

print("Fraud Probability:", fraud_prob[0][1])