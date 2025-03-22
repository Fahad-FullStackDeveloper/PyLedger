# Expense management
import streamlit as st
import sqlite3
from database import connect_db

def manage_expenses():
    st.subheader("Expense Manager")
    st.write("Track and categorize your expenses.")
    amount = st.number_input("Expense Amount", min_value=0, format="%.2f")
    category = st.text_input("Expense Category")
    description = st.text_area("Expense Description")
    if st.button("Add Expense"):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expnses (amount, category, description) VALUES (?,?,?)", (amount, category, description))
        conn.commit()
        conn.close()
        st.success("Expense added successfully!")
