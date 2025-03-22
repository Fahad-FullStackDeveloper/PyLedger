# Income management
import streamlit as st
import sqlite3
from database import connect_db

def manage_income():
    st.subheader("Income Manager")
    st.write("Add, view, and manage your income sources.")
    amount = st.number_input("Income Amount", min_value=0, format="%.2f")
    source = st.text_input("Income Source")
    description = st.text_area("Description")
    if st.button("Add Income"):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO income (amount, source, description) VALUES (?, ?, ?)", (amount, source, description))
        conn.commit()
        conn.close()
        st.success("Income added successfully!")
