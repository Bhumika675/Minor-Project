import pandas as pd

def generate_financial_summary(df):
    """Calculates overall metrics from the dataset."""

    total_income = df[df['Type'].str.lower() == 'income']['Amount'].sum()
    total_expense = df[df['Type'].str.lower() == 'expense']['Amount'].sum()
    net_savings = total_income - total_expense

    savings_rate = (net_savings / total_income) * 100 if total_income > 0 else 0
    
    # Category wise breakdown for Expenses
    expenses_df = df[df['Type'].str.lower() == 'expense']
    category_totals = expenses_df.groupby('Category')['Amount'].sum().sort_values(ascending=False).to_dict()
    
    return {
        "Total Income": total_income,
        "Total Expense": total_expense,
        "Net Savings": net_savings,
        "Savings Rate (%)": round(savings_rate, 2),
        "Category Breakdown": category_totals
    }