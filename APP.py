import streamlit as st
import pandas as pd 
import numpy as np
import os
from NP import calcular_monto, total_balance
from SQL import crear_tabla, añadir_transaccion, obtener_transacciones


st.title("GGP")
st.subheader("Gestión de Gastos Personales")

crear_tabla()

with st.form("Añadir Transacción", clear_on_submit=True):
    tipo = st.selectbox("Tipo de Transacción", ["Ingreso", "Gasto"])
    medio = st.selectbox("Medio de Pago", ["Efectivo", "Tarjeta de Crédito", "Transferencia Bancaria", "Otros"])
    monto = st.number_input("Monto", min_value=0.0, format="%.2f", step=1.0, placeholder="Ingrese el monto", value= None )
    categoria = st.selectbox("Categoría", ["Alimentos", "Transporte", "Entretenimiento", "Salud", "Educación", "Otros"])
    notas = st.text_input("Notas", placeholder="Opcional",)
 

    subido = st.form_submit_button("Añadir Transacción")
     

if subido:
    añadir_transaccion(
        tipo =  tipo,
        monto = monto,
        notas = notas,
        categoria = categoria
                       )
    st.success("Transacción añadida correctamente.")

df = obtener_transacciones()
st.metric(label="Balance Total", value=f"${total_balance(df):,.2f}")
st.dataframe(df)
