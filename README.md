# Budget Calculator

This is a simple budget calculator that helps you manage your finances by allowing you to input your income and expenses. It calculates your total income, total expenses, and net income, and provides visual representations of your expenses and budget through pie and bar charts.

## How to Use

1. Run the code in a Streamlit app or locally.
2. Input your income by entering the type of income and its amount in the corresponding text and number inputs provided. You can add multiple sources of income by clicking the "Add another income" button.
3. Add your expenses by entering the type of expense and its amount in the corresponding text and number inputs provided. You can add multiple expenses by clicking the "Add another expense" button.
4. Once you've entered all of your income and expenses, the app will automatically calculate your total income, total expenses, and net income.
5. The app will also display a pie chart of your income and expenses, as well as a bar chart of your budget.

## Understanding Your Budget

Your budget is divided into two main parts: income and expenses.

**Income** refers to the money you receive regularly, such as your salary, bonuses, or any other sources of income. In this app, you can input as many sources of income as you like.

**Expenses** refer to the money you spend regularly, such as rent, bills, groceries, or any other expenses. In this app, you can input as many expenses as you like.

Once you've inputted your income and expenses, the app will automatically calculate your total income and total expenses, and subtract your expenses from your income to give you your net income.

## Visualizing Your Budget

The app also provides visual representations of your budget through pie and bar charts.

The **pie chart** shows the proportion of your income and expenses. Each slice of the pie represents a category of income or expense, and the size of the slice represents the proportion of your budget that category makes up. 

The **bar chart** shows the amounts of your income, expenses, expected income (twice the amount of your expenses), and net income side by side. Each bar represents a category, and the height of the bar represents the amount of money in that category.

## Dependencies

This program requires the following Python packages:
- Streamlit
- Pandas
- Plotly Express

You can install them using pip:

```
pip install streamlit pandas plotly-express
```
