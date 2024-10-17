import streamlit as st
import pandas as pd

st.title("Wallet Tracker")

total_money = st.number_input("Enter your total money:", min_value = 0.0, step = 1.0)

if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns = ['Description', 'Amount', 'Category'])


def add_expense():
    new_expense = {
        'Description': st.text_input("Enter expense description:"),
        'Amount': st.number_input("Enter amount:"),
        'Category': st.selectbox("Select category:", ["Groceries", "Utilities", "Transportation", "Housing", "Health", "Pet Supplies & Care", "Entertainment", "Other"])
    }
    if st.button("Add Expense"):
        if new_expense['Description'] and new_expense['Amount'] != 0:
            new_expense_df = pd.DataFrame([new_expense])
            # Add the new expense with the existing expenses
            st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense_df], ignore_index = True)
            st.success("Expenses added!")
        else:
            st.error("Please enter valid information.")
    
add_expense()

# Display the expenses DataFrame
if not st.session_state.expenses.empty:
    st.subheader("Your Expenses:")
    st.dataframe(st.session_state.expenses)

    total_expenses = st.session_state.expenses['Amount'].sum()
    remaining_budget = total_money - total_expenses

    st.write(f"Your total expenses: {total_expenses:.2f}")
    st.write(f"Reamining budget: {remaining_budget:.2f}")

else:
    st.write("You have not entered any expenses yet.")