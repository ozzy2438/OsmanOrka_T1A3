# Financial Summary Terminal App

## Description
The Financial Summary Terminal App is a Python-based application that helps users track their income and expenses, set budgets, and view financial summaries with interactive visualizations.

## Features
1. Transaction Logging: Log income and expenses with categories, dates, and currencies.
2. Budget Management: Set and track budgets for different expense categories.
3. Financial Summary: View total income, expenses, and savings with interactive visualizations.
4. Date Range Filtering: View transactions within a specific date range.
5. Recurring Transactions: Set up recurring transactions for regular income or expenses.
6. Data Export: Export financial data for external analysis.
7. Interactive Dashboard: View a comprehensive financial dashboard with Plotly.
8. Live Updates: Start a live update mode to see real-time changes in your financial data.

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/ozzy2438/OsmanOrka_T1A3.git
   cd OsmanOrka_T1A3
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/modules/main.py
   ```
2. Follow the on-screen prompts to log transactions, set budgets, and view summaries.
3. When you choose to view the summary or interactive dashboard, the application will display charts and graphs using Plotly.

## System Requirements
- Python 3.7 or higher
- Required libraries: matplotlib, colorama, pandas, plotly

## File Structure
- `src/modules/`: Contains the main Python scripts (main.py, summary.py, transaction.py, budget.py, utils.py, recurring_transaction.py)
- `src/`: Contains setup and run scripts
- `requirements.txt`: Lists all the Python dependencies

## Testing
Manual testing procedures are available in the application. You can test various features by following the on-screen prompts.

## Contributing
Contributions to improve the Financial Summary Terminal App are welcome. Please feel free to submit pull requests or open issues for any bugs or feature requests.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.

# src/data/transactions.csv
Amount,Category,Type
100.00,Salary,income
50.00,Groceries,expense
30.00,Entertainment,expense
200.00,Freelance,income
75.00,Utilities,expense

# src/data/budgets.csv
Category,Limit
Groceries,200.00
Entertainment,100.00
Utilities,150.00

# docs/manual_testing.md
# Manual Testing Procedures

## 1. Transaction Logging
1. Run the application
2. Choose option 1 to log a transaction
3. Enter a valid amount (e.g., 50.00)
4. Enter a category (e.g., Food)
5. Enter the transaction type (income or expense)
6. Verify that the transaction is logged successfully
7. Repeat with invalid inputs to test error handling

## 2. Budget Management
1. Run the application
2. Choose option 2 to set a budget
3. Enter a category (e.g., Food)
4. Enter a budget limit (e.g., 300.00)
5. Verify that the budget is set successfully
6. Repeat with invalid inputs to test error handling

## 3. Financial Summary
1. Run the application
2. Log several transactions and set multiple budgets
3. Choose option 3 to view the financial summary
4. Verify that the total income, expenses, and savings are calculated correctly
5. Check that the expense distribution chart is displayed
6. Verify that the budget comparison chart is shown and reflects the set budgets and actual expenses

## 4. Data Persistence
1. Run the application and log several transactions and budgets
2. Exit the application
3. Run the application again
4. Verify that the previously entered data is still available

## 5. Error Handling
1. Test each input with invalid data (e.g., strings for numerical inputs)
2. Verify that appropriate error messages are displayed
3. Ensure that the application doesn't crash on invalid inputs

## 6. User Interface
1. Verify that the main menu is clear and easy to navigate
2. Check that all options work as expected
3. Ensure that the application provides clear feedback for all actions

Document the results of each test, including any bugs or issues encountered.