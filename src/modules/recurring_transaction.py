class RecurringTransaction:
    def __init__(self, amount, category, transaction_type, frequency):
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type
        self.frequency = frequency

    def __str__(self):
        return f"{self.frequency.capitalize()} {self.transaction_type}: ${self.amount:.2f} in {self.category}"
