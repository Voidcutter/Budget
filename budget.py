class Category:
    
    def __init__(self, name) -> None:
        self.name = name # name of a category (food, entertainment, etc.)
        self.ledger = [] # funds recordings

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def get_balance(self):
        balance = 0
        for record in self.ledger:
            balance += record['amount']
        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount   

    def withdraw(self, amount, description):
        if self.check_funds(amount) == True:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False


    