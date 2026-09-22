import streamlit as st
import pandas as pd 
import numpy as np
import os
from NP import calculate_amount, total_balance
from SQL import create_table, add_transaction, get_transactions


st.title("SpendManager")
st.subheader("Track your expenses and income easily")

#This will create the database and the table if they don't exist
create_table()

#Here the user can add a new transaction in the database.
with st.form("Add Transaction", clear_on_submit=True):
    type = st.selectbox("Transaction Type", ["Income", "Expense"])
    method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Bank Transfer", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f", step=1.0, placeholder="Enter the amount", value= None )
    category = st.selectbox("Category", ["Food", "Transportation", "Entertainment", "Health", "Education", "Other"])
    notes = st.text_input("Notes", placeholder="Optional",)
 

    submit = st.form_submit_button("Add Transaction")
     
#This section will start only if the sumbit button was pressed
if submit:
    add_transaction(
        type =  type,
        amount = amount,
        notes = notes,
        category = category
                       )
    st.success("Transaction added successfully.")

#This creates the df based on the transactions in the database
df = get_transactions()

#This shows the actual balance based on the database
st.metric(label="Total balance", value=f"${total_balance(df):,.2f}")
st.dataframe(df)
