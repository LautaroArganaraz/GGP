import numpy as np
import pandas as pd
import sqlite3 as sq
import streamlit as st

def calcular_monto(tipo: str, monto: float) -> float:
    if tipo == "Ingreso":
        return monto * 1
    else:
        return monto * -1

def total_balance(transacciones: pd.DataFrame) -> float:
    return transacciones['Monto'].sum()