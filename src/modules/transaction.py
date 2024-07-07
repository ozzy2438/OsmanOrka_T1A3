from datetime import date as date_class

class Transaction:
    def __init__(self, amount, category, transaction_type, date, currency='USD'):
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type
        self.date = date if isinstance(date, date_class) else date_class.fromisoformat(date)
        self.currency = currency

    def __str__(self):
        return f"{self.date.isoformat()} - {self.transaction_type.capitalize()}: {self.currency} {self.amount:.2f} in {self.category}"

class RecurringTransaction(Transaction):
    def __init__(self, date, description, amount, category, frequency):
        super().__init__(date, description, amount, category)
        self.frequency = frequency