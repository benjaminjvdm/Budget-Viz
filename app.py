import streamlit as st
import pandas as pd
import plotly.express as px

# Create a function to calculate the user's total income and expenses
def calculate_budget(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    net_income = total_income - total_expenses
    return total_income, total_expenses, net_income

# Create a function to display a pie chart of the user's expenses and income
def display_expenses_chart(income, expenses):
    total_income = sum(income)
    total_expenses = sum(expenses)
    
    expenses_df = pd.DataFrame({'Type': ['Income', 'Expenses'], 'Amount': [total_income, total_expenses]})
    colors = ['green', 'red']
    fig = px.pie(expenses_df, values='Amount', names='Type', title='Expenses vs Income', color_discrete_sequence=colors)
    st.plotly_chart(fig)

# Create a function to display a bar chart of the user's income and expenses
def display_budget_chart(total_income, total_expenses, net_income):
    expected_income = total_expenses * 2
    budget_df = pd.DataFrame({"Budget Type": ["Income", "Expenses", "Expected Income", "Net Income"], 
                              "Amount": [total_income, total_expenses, expected_income, net_income]})
    color_map = {"Income": "green", "Expenses": "red", "Expected Income": "blue", "Net Income": "purple"}
    fig = px.bar(budget_df, x="Budget Type", y="Amount", title="Budget", color="Budget Type", color_discrete_map=color_map)
    st.plotly_chart(fig)

# Create the Streamlit app
st.title("Budget Calculator")

# Get the user's income
st.subheader("Income")
income = []
income_counter = 0
while True:
    income_type = st.text_input(f"Enter the type of income {income_counter}", key=f"income_type_{income_counter}")
    income_amount = st.number_input(f"Enter the amount of income {income_counter}", step=1.0, key=f"income_amount_{income_counter}")
    income_counter += 1
    if income_type == "" or income_amount == 0:
        break
    income.append((income_type, income_amount))

# Get the user's expenses
st.subheader("Expenses")
expenses = []
expense_counter = 0
while True:
    expense_type = st.text_input(f"Enter the type of expense {expense_counter}", key=f"expense_type_{expense_counter}")
    expense_amount = st.number_input(f"Enter the amount of expense {expense_counter}", step=1.0, key=f"expense_amount_{expense_counter}")
    expense_counter += 1
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
display_expenses_chart([i[1] for i in income], [e[1] for e in expenses])
display_budget_chart(total_income, total_expenses, net_income)
