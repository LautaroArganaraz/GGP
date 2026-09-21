import sqlite3 as sq
from pathlib import Path
import pandas as pd


DB_PATH = Path(__file__).with_name("BSD.db")

def crear_tabla():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS transacciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL,
        monto REAL NOT NULL,
        notas TEXT,
        categoria TEXT
    )
    """
    with sq.connect(DB_PATH) as conn:
        conn.execute(create_table_query)

def añadir_transaccion(tipo, monto, notas, categoria):
    insert_query = """
    INSERT INTO transacciones (tipo, monto, notas, categoria)
    VALUES (?, ?, ?, ?)
    """
    with sq.connect(DB_PATH) as conn:
        conn.execute(insert_query, (tipo, monto, notas, categoria))

def obtener_transacciones():
    query = """
    SELECT tipo AS Tipo, monto AS Monto, notas AS Notas, categoria AS Categoría
    FROM transacciones
    ORDER BY id DESC
    """
    with sq.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn)