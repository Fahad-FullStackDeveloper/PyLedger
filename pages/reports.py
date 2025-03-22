# Financial reports
import streamlit as st
import sqlite3
from database import connect_db

def generate_report():
    st.subheader("Financial Report")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = curson.fetchone()[0] or 0
    curson.execute("SELECT SUM(amount) FROM expenses")
    total_expenses = cursor.fetchone()[0] or 0
    conn.close()
    st.write(f"Total Income: ${total_income:.2f}")
    st.write(f"Total Expenses: ${total_expense:.2f}")
    st.write(f"Net Balance: ${total_income - total_expense:.2f}")

    
# def generate_reports():
#     st.subheader("Financial Reports")
#     st.write("View your financial reports here.")
#     st.sidebar.subheader("Filter Reports")
#     st.sidebar.date_input("Start date", min_value=None, max_value=None)
#     st.sidebar.date_input("End date", min_value=None, max_value=None)
#     with st.sidebar.form("report_form"):
#         st.selectbox("Select report type", ["Income", "Expense", "Balance"])
#         st.selectbox("Category", ["All", "Category1", "Category2", "Category3"])
#         submit_button = st.form_submit_button("Generate Report")
#         if submit_button:
#             start_date = st.sidebar.form_date("report_form", "start_date")
#             end_date = st.sidebar.form_date("report_form", "end_date")
#             report_type = st.sidebar.form_selectbox("report_form", "report_type", ["Income", "Expense", "Balance"])
#             category = st.sidebar.form_selectbox("report_form", "category", ["All", "Category1", "Category2", "Category3"])
#             generate_report(start_date, end_date, report_type, category)
#             st.success("Report generated successfully!")
#         st.sidebar.markdown("---")
#     st.sidebar.button("Export Report")
#     st.markdown("---")
#     st.subheader("Income vs. Expense")
#     st.line_chart(get_income_expense_chart())
#     st.subheader("Monthly Balance")
#     st.line_chart(get_monthly_balance_chart())
#     st.subheader("Top 5 Categories")
#     st.table(get_top_categories())
#     st.subheader("Income vs. Expense by Category")
#     st.bar_chart(get_income_expense_by_category_chart())

# def generate_report(start_date, end_date, report_type, category):
#     conn = connect_db()
#     cur = conn.cursor()
#     if report_type == "Income":
#         cur.execute("SELECT * FROM transactions WHERE date >=? AND date <=? AND type =?", (start_date, end_date, "Income"))
#     elif report_type == "Expense":
#         cur.execute("SELECT * FROM transactions WHERE date >=? AND date <=? AND type =?", (start_date, end_date, "Expense"))
#     else:
#         cur.execute("SELECT * FROM transactions WHERE date >=? AND date <=?", (start_date, end_date))
#     if category!= "All":
#         cur.execute("SELECT * FROM transactions WHERE date >=? AND date <=? AND type =? AND category =?", (start_date, end_date, report_type, category))
#     transactions = cur.fetchall()
#     conn.close()
#     return transactions

 