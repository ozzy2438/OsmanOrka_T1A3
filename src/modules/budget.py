import csv
import os

class Budget:
    def __init__(self):
        self.budgets = {}

    def set_budget(self, category, limit):
        self.budgets[category] = float(limit)

    def get_budget(self, category):
        return self.budgets.get(category, 0)

    def load_budgets(self, filename):
        file_path = os.path.join('data', filename)
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    self.set_budget(row[0], float(row[1]))

    def save_budgets(self, filename):
        file_path = os.path.join('data', filename)
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Category', 'Limit'])
            for category, limit in self.budgets.items():
                writer.writerow([category, limit])