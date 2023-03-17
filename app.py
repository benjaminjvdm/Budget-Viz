import streamlit as st
import pandas as pd
import plotly.express as px

# Create a function to calculate the user's total income and expenses
def calculate_budget(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    net_income = total_income - total_expenses
    return total_income, total_expenses, net_income

# Create a function to display a pie chart of the user's expenses
def display_expenses_chart(expenses):
    expenses_df = pd.DataFrame(expenses, columns=["Expense Type", "Amount"])
    fig = px.pie(expenses_df, values="Amount", names="Expense Type", title="Expenses")
    st.plotly_chart(fig)

# Create a function to display a bar chart of the user's income and expenses
def display_budget_chart(total_income, total_expenses, net_income):
    expected_income = total_expenses * 3
    budget_df = pd.DataFrame({"Budget Type": ["Income", "Expenses", "Expected Income", "Net Income"], 
                              "Amount": [total_income, total_expenses, expected_income, net_income]})
    fig = px.bar(budget_df, x="Budget Type", y="Amount", title="Budget")
    st.plotly_chart(fig)

# Create the Streamlit app
st.title("Budget Calculator")

# Get the user's income
st.subheader("Income")
income = []
while True:
    income_type = st.text_input("Enter the type of income")
    income_amount = st.number_input("Enter the amount of income", step=100.0)
    if income_type == "" or income_amount == 0:
        break
    income.append((income_type, income_amount))

# Get the user's expenses
st.subheader("Expenses")
expenses = []
while True:
    expense_type = st.text_input("Enter the type of expense", key='expense_type')
    expense_amount = st.number_input("Enter the amount of expense", step=100.0, key='expense_amount')
    if expense_type == "" or expense_amount == 0:
        break
    expenses.append((expense_type, expense_amount))

# Calculate the user's budget and display it
total_income, total_expenses, net_income = calculate_budget([i[1] for i in income], [e[1] for e in expenses])
st.subheader("Budget")
st.write(f"Total Income: ${total_income:.2f}")
st.write(f"Total Expenses: ${total_expenses:.2f}")
st.write(f"Net Income: ${net_income:.2f}")

# Display charts of the user's expenses and budget
display_expenses_chart(expenses)
display_budget_chart(total_income, total_expenses, net_income)
