import os
import csv
from datetime import datetime
import pandas as pd

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, data_type):
    while True:
        try:
            return data_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")

def load_data(filename, class_type):
    data = []
    file_path = os.path.join('data', filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                data.append(class_type(*row))
    return data

def save_data(filename, data):
    file_path = os.path.join('data', filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].__dict__.keys())  # Write header
        for item in data:
            writer.writerow(item.__dict__.values())

def save_recurring_transaction(transaction):
    file_path = os.path.join('data', 'recurring_transactions.csv')
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if os.path.getsize(file_path) == 0:
            writer.writerow(['amount', 'category', 'transaction_type', 'frequency'])
        writer.writerow([transaction.amount, transaction.category, transaction.transaction_type, transaction.frequency])

def export_data(transactions, budget):
    # Export transactions
    with open('exported_transactions.csv', 'w') as f:
        f.write('Date,Amount,Category,Type\n')
        for t in transactions:
            f.write(f'{t.date},{t.amount},{t.category},{t.transaction_type}\n')
    
    # Export budgets
    with open('exported_budgets.csv', 'w') as f:
        f.write('Category,Limit\n')
        for category, limit in budget.budgets.items():
            f.write(f'{category},{limit}\n')

def validate_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def validate_currency(amount):
    try:
        return float(amount)
    except ValueError:
        raise ValueError("Invalid amount. Please enter a valid number.")