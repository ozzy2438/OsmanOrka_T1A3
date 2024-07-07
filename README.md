
# Financial Summary Terminal App

## Description
The Financial Summary Terminal App is a Python-based application that helps users track their income and expenses, set budgets, and view financial summaries with visualizations.

## Features
1. Transaction Logging: Log income and expenses with categories.
2. Budget Management: Set and track budgets for different expense categories.
3. Financial Summary: View total income, expenses, and savings with visualizations.

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/T1A3-Financial-Summary.git
   cd financial-summary
   ```
2. Run the setup script:
   ```
   ./src/setup.sh
   ```

## Usage
1. Run the application:
   ```
   ./src/run.sh
   ```
2. Follow the on-screen prompts to log transactions, set budgets, and view summaries.
3. When you choose to view the summary, the application will display charts and graphs.

## System Requirements
- Python 3.7 or higher
- matplotlib library

## File Structure
- `src/modules/`: Contains the main Python scripts
- `src/data/`: Stores CSV files for transactions and budgets
- `docs/manual_testing.md`: Contains manual testing procedures

## Testing
Refer to `docs/manual_testing.md` for testing procedures and results.

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

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