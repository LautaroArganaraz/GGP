import sqlite3 as sq
from pathlib import Path
import pandas as pd


DB_PATH = Path(__file__).with_name("database.db")

#This query creates the transactions table if it doesn't exist
def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        notes TEXT,
        category TEXT
    )
    """
    with sq.connect(DB_PATH) as conn:
        conn.execute(create_table_query)

#This query will add the transaction in the database
def add_transaction(type, amount, notes, category):
    insert_query = """
    INSERT INTO transactions (type, amount, notes, category)
    VALUES (?, ?, ?, ?)
    """
    with sq.connect(DB_PATH) as conn:
        conn.execute(insert_query, (type, amount, notes, category))

#This query gets all of the transactions
def get_transactions():
    query = """
    SELECT type AS Type, amount AS Amount, notes AS Notes, category AS Category
    FROM transactions
    ORDER BY id DESC
    """
    with sq.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn)