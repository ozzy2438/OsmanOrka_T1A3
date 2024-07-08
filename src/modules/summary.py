import matplotlib.pyplot as plt
from colorama import Fore, Style
import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import threading
import time

class Summary:
    def __init__(self):
        self.update_interval = 5  # 5 saniyede bir güncelle
        self.stop_update = False
        self.update_thread = None

    def generate_summary(self, transactions, budget):
        income = sum(t.amount for t in transactions if t.transaction_type == 'income')
        expenses = sum(abs(t.amount) for t in transactions if t.transaction_type == 'expense')
        savings = income - expenses

        currencies = set(t.currency for t in transactions)
        for currency in currencies:
            currency_income = sum(t.amount for t in transactions if t.transaction_type == 'income' and t.currency == currency)
            currency_expenses = sum(abs(t.amount) for t in transactions if t.transaction_type == 'expense' and t.currency == currency)
            currency_savings = currency_income - currency_expenses

            print(Fore.CYAN + Style.BRIGHT + f"Total Income ({currency}): {currency} {currency_income:.2f}")
            print(Fore.CYAN + Style.BRIGHT + f"Total Expenses ({currency}): {currency} {currency_expenses:.2f}")
            print(Fore.CYAN + Style.BRIGHT + f"Total Savings ({currency}): {currency} {currency_savings:.2f}")

            if currency_income > 0:
                savings_rate = (currency_savings / currency_income) * 100
                print(Fore.CYAN + Style.BRIGHT + f"Savings Rate ({currency}): %{savings_rate:.2f}")

        self.generate_expense_chart(transactions)
        self.generate_budget_comparison(transactions, budget)
        self.generate_monthly_trend(transactions)

    def generate_expense_chart(self, transactions):
        categories = {}
        for t in transactions:
            if t.transaction_type == 'expense':
                categories[t.category] = categories.get(t.category, 0) + abs(t.amount)

        fig = go.Figure(data=[go.Pie(labels=list(categories.keys()), values=list(categories.values()))])
        fig.update_layout(title_text="Expense Distribution", template="plotly_dark")
        fig.show()

    def generate_budget_comparison(self, transactions, budget):
        actual_expenses = {}
        for t in transactions:
            if t.transaction_type == 'expense':
                actual_expenses[t.category] = actual_expenses.get(t.category, 0) + abs(t.amount)

        categories = list(set(list(actual_expenses.keys()) + list(budget.budgets.keys())))
        actual = [actual_expenses.get(cat, 0) for cat in categories]
        budgeted = [budget.get_budget(cat) for cat in categories]

        fig = make_subplots(rows=2, cols=1, specs=[[{'type':'bar'}], [{'type':'pie'}]])

        fig.add_trace(go.Bar(x=categories, y=actual, name="Actual", marker_color='#ff9999'), row=1, col=1)
        fig.add_trace(go.Bar(x=categories, y=budgeted, name="Budgeted", marker_color='#66b3ff'), row=1, col=1)

        total_budget = sum(budgeted)
        budget_percentages = [b/total_budget*100 for b in budgeted]
        fig.add_trace(go.Pie(labels=categories, values=budget_percentages), row=2, col=1)

        fig.update_layout(title_text="Budget Comparison", height=800, template="plotly_dark")
        fig.show()

        # Print detailed comparison
        print("\nDetailed Budget Comparison:")
        print(f"{'Category':<15} {'Budgeted':>10} {'Actual':>10} {'Difference':>12} {'% Used':>10}")
        print("-" * 60)
        for cat, bud, act in zip(categories, budgeted, actual):
            diff = bud - act
            percent_used = (act / bud * 100) if bud > 0 else 0
            print(f"{cat:<15} ${bud:>9.2f} ${act:>9.2f} ${diff:>11.2f} {percent_used:>9.1f}%")

        total_budgeted = sum(budgeted)
        total_actual = sum(actual)
        total_diff = total_budgeted - total_actual
        total_percent = (total_actual / total_budgeted * 100) if total_budgeted > 0 else 0
        print("-" * 60)
        print(f"{'TOTAL':<15} ${total_budgeted:>9.2f} ${total_actual:>9.2f} ${total_diff:>11.2f} {total_percent:>9.1f}%")

    def generate_monthly_trend(self, transactions):
        monthly_data = {}
        for t in transactions:
            month_key = t.date.strftime("%Y-%m")
            if month_key not in monthly_data:
                monthly_data[month_key] = {"income": 0, "expense": 0}
            monthly_data[month_key][t.transaction_type] += t.amount

        months = sorted(monthly_data.keys())
        income = [monthly_data[m]["income"] for m in months]
        expenses = [monthly_data[m]["expense"] for m in months]
        savings = [inc - exp for inc, exp in zip(income, expenses)]

        fig = make_subplots(rows=2, cols=1)

        fig.add_trace(go.Scatter(x=months, y=income, mode='lines+markers', name='Income'), row=1, col=1)
        fig.add_trace(go.Scatter(x=months, y=expenses, mode='lines+markers', name='Expense'), row=1, col=1)
        fig.add_trace(go.Scatter(x=months, y=savings, mode='lines+markers', name='Savings'), row=1, col=1)

        fig.add_trace(go.Bar(x=months, y=income, name='Income'), row=2, col=1)
        fig.add_trace(go.Bar(x=months, y=expenses, name='Expense'), row=2, col=1)

        fig.update_layout(title_text="Monthly Trends", height=800, template="plotly_dark")
        fig.show()

    def start_live_update(self, transactions, budget):
        self.update_thread = threading.Thread(target=self.update_data, args=(transactions, budget))
        self.update_thread.start()

    def stop_live_update(self):
        self.stop_update = True
        if self.update_thread:
            self.update_thread.join()

    def update_data(self, transactions, budget):
        while not self.stop_update:
            self.generate_summary(transactions, budget)
            time.sleep(self.update_interval)

    def generate_interactive_dashboard(self, transactions, budget):
        df = pd.DataFrame([(t.date, t.amount, t.category, t.transaction_type, t.currency) for t in transactions],
                          columns=['Date', 'Amount', 'Category', 'Type', 'Currency'])
        
        fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'pie'}, {'type': 'bar'}],
                                                   [{'type': 'scatter'}, {'type': 'table'}]])

        # Expense Distribution
        expense_data = df[df['Type'] == 'expense'].groupby('Category')['Amount'].sum()
        fig.add_trace(go.Pie(labels=expense_data.index, values=expense_data.values, name="Expenses"), row=1, col=1)

        # Budget Comparison
        actual_expenses = df[df['Type'] == 'expense'].groupby('Category')['Amount'].sum()
        budgeted = pd.Series({cat: budget.get_budget(cat) for cat in actual_expenses.index})
        fig.add_trace(go.Bar(x=actual_expenses.index, y=actual_expenses.values, name="Actual"), row=1, col=2)
        fig.add_trace(go.Bar(x=budgeted.index, y=budgeted.values, name="Budgeted"), row=1, col=2)

        # Monthly Trend
        monthly_data = df.groupby([df['Date'].dt.to_period('M'), 'Type'])['Amount'].sum().unstack()
        fig.add_trace(go.Scatter(x=monthly_data.index.astype(str), y=monthly_data['income'], name="Income"), row=2, col=1)
        fig.add_trace(go.Scatter(x=monthly_data.index.astype(str), y=monthly_data['expense'], name="Expense"), row=2, col=1)

        # Recent Transactions Table
        recent_transactions = df.sort_values('Date', ascending=False).head(10)
        fig.add_trace(go.Table(
            header=dict(values=list(recent_transactions.columns)),
            cells=dict(values=[recent_transactions[col] for col in recent_transactions.columns])
        ), row=2, col=2)

        fig.update_layout(height=800, title_text="Interactive Financial Dashboard", template="plotly_dark")
        fig.show()