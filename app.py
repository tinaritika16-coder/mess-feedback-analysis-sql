import streamlit as st
import pandas as pd
import sqlite3
import joblib

st.title("Mess Feedback Analysis Dashboard (SQL Powered)")

conn = sqlite3.connect("mess_feedback.db")
df = pd.read_sql_query("SELECT * FROM mess_feedback", conn)
conn.close()

st.subheader("Live Data Preview")
st.dataframe(df.head())

log_model = joblib.load("logistic_model.pkl")
rf_model = joblib.load("random_forest_model.pkl")

st.subheader("Predict Student Satisfaction")

food = st.selectbox("Food Quality", ["Poor", "Average", "Good"])
clean = st.selectbox("Cleanliness", ["Poor", "Average", "Good"])
menu = st.selectbox("Menu Variety", ["Poor", "Average", "Good"])
wait = st.selectbox("Waiting Time", ["Long", "Medium", "Short"])
staff = st.selectbox("Staff Behavior", ["Bad", "Okay", "Good"])

input_data = pd.DataFrame([{
    "Food_Quality": food,
    "Cleanliness": clean,
    "Menu_Variety": menu,
    "Waiting_Time_Rating": wait,
    "Staff_Behavior": staff
}])

if st.button("Predict"):
    log_pred = log_model.predict(input_data)[0]
    rf_pred = rf_model.predict(input_data)[0]

    st.success(f"Logistic Regression Prediction: {log_pred}")
    st.success(f"Random Forest Prediction: {rf_pred}")
