
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("student_performance.csv")
print(df.head())
df.describe()



X = df[['Hours_Studied', 'Attendance', 'Previous_Score']]
y = df['Pass']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)


model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)



pred_lr = model_lr.predict(X_test)
pred_rf = model_rf.predict(X_test)

print("LR Accuracy:", accuracy_score(y_test, pred_lr))
print("RF Accuracy:", accuracy_score(y_test, pred_rf))

# Save the better performing model
lr_accuracy = accuracy_score(y_test, pred_lr)
rf_accuracy = accuracy_score(y_test, pred_rf)

if rf_accuracy >= lr_accuracy:
    joblib.dump(model_rf, "student_model.pkl")
    print(f"\n✓ Saved Random Forest model (Accuracy: {rf_accuracy:.2%})")
else:
    joblib.dump(model_lr, "student_model.pkl")
    print(f"\n✓ Saved Logistic Regression model (Accuracy: {lr_accuracy:.2%})")
