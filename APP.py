import streamlit as st
import pandas as pd 
import numpy as np
import os
from NP import calcular_monto, total_balance
from SQL import crear_tabla, añadir_transaccion, obtener_transacciones


st.title("SpendManager")
st.subheader("Track your expenses and income easily")

crear_tabla()

with st.form("Add Transaction", clear_on_submit=True):
    type = st.selectbox("Transaction Type", ["Income", "Expense"])
    method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Bank Transfer", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f", step=1.0, placeholder="Enter the amount", value= None )
    category = st.selectbox("Category", ["Food", "Transportation", "Entertainment", "Health", "Education", "Other"])
    notes = st.text_input("Notes", placeholder="Optional",)
 

    subido = st.form_submit_button("Add Transaction")
     

if subido:
    añadir_transaccion(
        type =  type,
        amount = amount,
        notes = notes,
        category = category
                       )
    st.success("Transaction added successfully.")

df = obtener_transacciones()
st.metric(label="Balance Total", value=f"${total_balance(df):,.2f}")
st.dataframe(df)
