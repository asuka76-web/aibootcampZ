# pages/1_Retirement_Simulator.py

import streamlit as st

st.set_page_config(page_title="CPF Retirement Simulator", layout="wide")
st.title("🧓 CPF Retirement Planning Simulator")

st.markdown("Simulate your retirement savings based on CPF policies.")

# --- User Inputs ---
age = st.slider("Your current age", 21, 65, 30)
retirement_age = st.slider("Planned retirement age", 55, 70, 65)
current_savings = st.number_input("Current CPF savings ($)", min_value=0, value=20000)
monthly_contribution = st.number_input("Monthly CPF contribution ($)", min_value=0, value=1200)
expected_rate = st.slider("Expected annual interest rate (%)", 0.0, 6.0, 4.0)

years_to_save = retirement_age - age

# --- Simulation Calculation ---
future_value = current_savings
for _ in range(years_to_save * 12):
    future_value += monthly_contribution
    future_value *= (1 + (expected_rate / 100) / 12)

# --- Display Result ---
st.subheader("💰 Estimated CPF Savings at Retirement:")
st.success(f"${future_value:,.2f}")
