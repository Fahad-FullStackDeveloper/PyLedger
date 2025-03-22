# Handles SQLite DB
import sqlite3

def connect_db():
    conn = sqlite3.connect("accounting.db")
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

create_tables()