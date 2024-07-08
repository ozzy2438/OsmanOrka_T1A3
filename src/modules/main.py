import sys
from datetime import datetime
from transaction import Transaction, RecurringTransaction
from budget import Budget
from summary import Summary
from utils import clear_screen, get_user_input, load_data, save_data, save_recurring_transaction, export_data
from colorama import init, Fore, Style

init(autoreset=True)

def main():
    transactions = load_data('transactions.csv', Transaction)
    budget = Budget()
    budget.load_budgets('budgets.csv')
    summary = Summary()

    # Add sample data if no data exists
    if not transactions:
        transactions.extend([
            Transaction(1000, "Salary", "income", "2023-05-01", "USD"),
            Transaction(100, "Groceries", "expense", "2023-05-02", "USD"),
            Transaction(50, "Entertainment", "expense", "2023-05-03", "USD"),
            Transaction(200, "Rent", "expense", "2023-05-04", "USD"),
            Transaction(30, "Transportation", "expense", "2023-05-05", "USD"),
        ])
        save_data('transactions.csv', transactions)

    if not budget.budgets:
        budget.set_budget("Groceries", 150)
        budget.set_budget("Entertainment", 100)
        budget.set_budget("Rent", 300)
        budget.set_budget("Transportation", 50)
        budget.save_budgets('budgets.csv')

    while True:
        clear_screen()
        print("\nFinancial Summary Terminal App")
        print("1. Log Transaction")
        print("2. Set Budget")
        print("3. View Summary")
        print("4. View Transactions by Date Range")
        print("5. Set Recurring Transaction")
        print("6. Export Data")
        print("7. View Interactive Dashboard")
        print("8. Start Live Update")
        print("9. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if not choice:
            print("Please enter a valid choice.")
            continue

        if choice == "1":
            amount = get_user_input("Enter amount: ", float)
            category = get_user_input("Enter category: ", str)
            transaction_type = get_user_input("Enter type (income/expense): ", str).lower()
            date = get_user_input("Enter date (YYYY-MM-DD): ", lambda x: datetime.strptime(x, "%Y-%m-%d").date())
            currency = get_user_input("Enter currency (default: USD): ", str) or "USD"
            
            if transaction_type not in ['income', 'expense']:
                print(Fore.RED + "Invalid transaction type. Please enter 'income' or 'expense'.")
                continue

            transaction = Transaction(amount, category, transaction_type, date, currency)
            transactions.append(transaction)
            save_data('transactions.csv', transactions)
            print(Fore.GREEN + "Transaction added successfully!")

        elif choice == "2":
            category = get_user_input("Enter category: ", str)
            limit = get_user_input("Enter budget limit: ", float)
            budget.set_budget(category, limit)
            budget.save_budgets('budgets.csv')
            print(Fore.GREEN + f"Budget set for {category}: ${limit}")
            update_choice = input("Do you want to update other categories? (y/n): ").lower()
            while update_choice == 'y':
                category = get_user_input("Enter category: ", str)
                limit = get_user_input("Enter budget limit: ", float)
                budget.set_budget(category, limit)
                budget.save_budgets('budgets.csv')
                print(Fore.GREEN + f"Budget set for {category}: ${limit}")
                update_choice = input("Do you want to update other categories? (y/n): ").lower()

        elif choice == "3":
            summary.generate_summary(transactions, budget)

        elif choice == "4":
            start_date = get_user_input("Enter start date (YYYY-MM-DD): ", lambda x: datetime.strptime(x, "%Y-%m-%d").date())
            end_date = get_user_input("Enter end date (YYYY-MM-DD): ", lambda x: datetime.strptime(x, "%Y-%m-%d").date())
            filtered_transactions = [t for t in transactions if start_date <= t.date <= end_date]
            for transaction in filtered_transactions:
                print(Fore.CYAN + str(transaction))

        elif choice == "5":
            amount = get_user_input("Enter amount: ", float)
            category = get_user_input("Enter category: ", str)
            transaction_type = get_user_input("Enter type (income/expense): ", str).lower()
            frequency = get_user_input("Enter frequency (daily/weekly/monthly): ", str).lower()
            
            if transaction_type not in ['income', 'expense']:
                print(Fore.RED + "Invalid transaction type. Please enter 'income' or 'expense'.")
                continue
            
            if frequency not in ['daily', 'weekly', 'monthly']:
                print(Fore.RED + "Invalid frequency. Please enter 'daily', 'weekly', or 'monthly'.")
                continue
            
            recurring_transaction = RecurringTransaction(amount, category, transaction_type, frequency)
            save_recurring_transaction(recurring_transaction)
            print(Fore.GREEN + "Recurring transaction set successfully!")

        elif choice == "6":
            export_data(transactions, budget)
            print(Fore.GREEN + "Data exported successfully!")

        elif choice == "7":
            summary.generate_interactive_dashboard(transactions, budget)

        elif choice == "8":
            summary.start_live_update(transactions, budget)
            input("Press Enter to stop live update...")
            summary.stop_live_update()

        elif choice == "9":
            print(Fore.GREEN + "Thank you for using the Financial Summary Terminal App!")
            sys.exit(0)

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

        input(Fore.YELLOW + "Press Enter to continue...")

if __name__ == "__main__":
    main()