import streamlit as st
import joblib

model = joblib.load("house_model.pkl")

st.title("House Price Predictor")

area = st.number_input("Enter Area")

if st.button("Predict"):

    price = model.predict([[area]])

    st.success(f"Predicted Price: ₹{price[0]:,.0f}")