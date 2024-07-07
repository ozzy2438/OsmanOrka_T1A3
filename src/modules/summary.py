import matplotlib.pyplot as plt
from colorama import Fore, Style
import numpy as np

class Summary:
    def generate_summary(self, transactions, budget):
        income = sum(t.amount for t in transactions if t.transaction_type == 'income')
        expenses = sum(t.amount for t in transactions if t.transaction_type == 'expense')
        savings = income - expenses

        currencies = set(t.currency for t in transactions)
        for currency in currencies:
            currency_income = sum(t.amount for t in transactions if t.transaction_type == 'income' and t.currency == currency)
            currency_expenses = sum(t.amount for t in transactions if t.transaction_type == 'expense' and t.currency == currency)
            currency_savings = currency_income - currency_expenses

            print(Fore.CYAN + Style.BRIGHT + f"Total Income ({currency}): {currency} {currency_income:.2f}")
            print(Fore.CYAN + Style.BRIGHT + f"Total Expenses ({currency}): {currency} {currency_expenses:.2f}")
            print(Fore.CYAN + Style.BRIGHT + f"Total Savings ({currency}): {currency} {currency_savings:.2f}")

            if currency_income > 0:
                savings_rate = (currency_savings / currency_income) * 100
                print(Fore.CYAN + Style.BRIGHT + f"Savings Rate ({currency}): {savings_rate:.2f}%")

        self.generate_expense_chart(transactions)
        self.generate_budget_comparison(transactions, budget)
        self.generate_monthly_trend(transactions)

    def generate_expense_chart(self, transactions):
        categories = {}
        for t in transactions:
            if t.transaction_type == 'expense':
                categories[t.category] = categories.get(t.category, 0) + t.amount

        plt.figure(figsize=(10, 6))
        plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.show()

    def generate_budget_comparison(self, transactions, budget):
        actual_expenses = {}
        for t in transactions:
            if t.transaction_type == 'expense':
                actual_expenses[t.category] = actual_expenses.get(t.category, 0) + t.amount

        categories = list(set(list(actual_expenses.keys()) + list(budget.budgets.keys())))
        actual = [actual_expenses.get(cat, 0) for cat in categories]
        budgeted = [budget.get_budget(cat) for cat in categories]

        if not categories:
            print("No data available for budget comparison.")
            return

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))
        x = range(len(categories))
        width = 0.35

        # Bar chart
        ax1.bar([i - width/2 for i in x], actual, width, label='Actual', color='#ff9999')
        ax1.bar([i + width/2 for i in x], budgeted, width, label='Budgeted', color='#66b3ff')

        ax1.set_xlabel('Categories')
        ax1.set_ylabel('Amount')
        ax1.set_title('Budget vs Actual Expenses')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories, rotation=45, ha='right')
        ax1.legend()

        # Add value labels on bars
        for i, v in enumerate(actual):
            ax1.text(i - width/2, v, f'${v:.2f}', ha='center', va='bottom')
        for i, v in enumerate(budgeted):
            ax1.text(i + width/2, v, f'${v:.2f}', ha='center', va='bottom')

        # Pie chart for budget allocation
        total_budget = sum(budgeted)
        budget_percentages = [b/total_budget*100 for b in budgeted]
        colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
        ax2.pie(budget_percentages, labels=categories, autopct='%1.1f%%', startangle=90, colors=colors)
        ax2.set_title('Budget Allocation')

        plt.tight_layout()
        plt.show()

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

        if not months:
            print("No data available for monthly trend.")
            return

        plt.figure(figsize=(12, 8))
        plt.subplot(2, 1, 1)
        plt.plot(months, income, label='Income', marker='o', color='g')
        plt.plot(months, expenses, label='Expenses', marker='o', color='r')
        plt.plot(months, savings, label='Savings', marker='o', color='b')
        plt.title('Monthly Income, Expenses, and Savings Trend')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 1, 2)
        width = 0.35
        x = range(len(months))
        plt.bar([i - width/2 for i in x], income, width, label='Income', color='g', alpha=0.7)
        plt.bar([i + width/2 for i in x], expenses, width, label='Expenses', color='r', alpha=0.7)
        plt.title('Monthly Income vs Expenses')
        plt.xlabel('Month')
        plt.ylabel('Amount')
        plt.legend()
        plt.xticks(x, months, rotation=45)
        plt.grid(True)

        plt.tight_layout()
        plt.show()