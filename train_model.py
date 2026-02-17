import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

conn = sqlite3.connect("mess_feedback.db")
df = pd.read_sql_query("SELECT * FROM mess_feedback", conn)
conn.close()

X = df.drop("Overall_Satisfaction", axis=1)
y = df["Overall_Satisfaction"]

categorical_cols = X.columns.tolist()

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

log_model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression())
])

rf_model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

log_model.fit(X_train, y_train)
rf_model.fit(X_train, y_train)

print("Logistic Regression Report:\n", classification_report(y_test, log_model.predict(X_test)))
print("Random Forest Report:\n", classification_report(y_test, rf_model.predict(X_test)))

joblib.dump(log_model, "logistic_model.pkl")
joblib.dump(rf_model, "random_forest_model.pkl")

print("Models trained and saved!")
