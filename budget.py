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

    def withdraw(self, amount, description=''):
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
    
    # on printing an object
    def __str__(self): 
        # create a category title surrounded by 30 * symbols. ^ means the category name is centered:
        result = f'{self.name:*^30}\n'  

        for record in self.ledger:
            # check the two decimals thing in the amount:
            amount = f"{record['amount']:.2f}" 
            result += f'{record["description"][:23]: <23}{amount: >7}' + '\n'
        result += f'Total: {self.get_balance():.2f}'
        return result

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

print(food)
        


    