import streamlit as st
from auth import login, signup
from pages.dashboard import show_dashboard

def main():
    st.title("Accounting App v1.1")
    menu = ["Login", "Sign Up"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Login":
        user = login()
        if user:
            show_main_page(user)
    elif choice == "Sign Up":
        signup()

def show_main_page(user):
    st.sidebar.write(f"Logger in as:{user}")
    st.sidebar.write("Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Income", "Expense", "Reports"])

    if page == "Dashboard":
        show_dashboard()
    elif page == "Income":
        from pages.income import manage_income
        manage_income()
    elif page == "Expense":
        from pages.expense import manage_expenses
        manage_expense()
    elif page == "Reports":
        from pages.reports import generate_reports
        generate_reports()

if __name__ == "__main__":
    main()