# Accounting App using Streamlit
Accounting App v1.0
===================

Description:
------------
This is a simple accounting application built using Streamlit with SQLite for database management. It includes user authentication and modules for managing income, expenses, and generating financial reports.

Features:
---------
- User authentication (Login/Signup)
- Dashboard overview
- Income & Expense management
- Financial reports generation
- SQLite database support

## 📌 Overview
This is a **personal finance management application** built using **Python and Streamlit**. It allows users to:
- **Track Income and Expenses** 📊
- **Visualize Financial Data** with Charts 📈
- **Manage Transactions** 📝
- **User Authentication** (Login/Signup) 🔑

## 🚀 Features
- **User Authentication**: Secure login & signup with hashed passwords.
- **Income & Expense Management**: Add, view, and track transactions.
- **Transaction History**: View and manage all income/expense entries.
- **Data Visualization**: Bar & line charts for financial insights.
- **Monthly & Yearly Tracking**: Analyze financial trends over time.

## 📂 Project Structure
```
accounting_app/
│── main.py          # Main Streamlit app
│── database.py      # Handles SQLite DB
│── auth.py          # Manages user login/signup
│── pages/
│   ├── dashboard.py  # Overview page
│   ├── income.py     # Income management
│   ├── expense.py    # Expense management
│   ├── reports.py    # Financial reports
│── assets/          # Store static files like receipts
│── requirements.txt # Dependencies
```

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/accounting-app.git
   cd accounting-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

Contributors:
-------------
Fahad Khakwani (Python Engineer)


## 🛠 Tech Stack
- **Python** 🐍
- **Streamlit** 🌐 (for UI)
- **SQLite** 🗄️ (for data storage)
- **Plotly** 📊 (for data visualization)

## 📌 Usage
1. **Sign up** for a new account or **log in**.
2. Add **income and expenses** with date and category.
3. View **transaction history** and **visualized insights**.
4. Track financial growth with **monthly reports**.

## 🔒 Security
- Passwords are securely hashed using **bcrypt**.
- SQLite database stores user credentials and transactions.

## 📞 Support
For any issues, please open a GitHub issue or contact [your-email@example.com](mailto:your-email@example.com).

