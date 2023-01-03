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
    
    def get_withdraw(self):
        withdraw = 0
        for record in self.ledger:
            if record['amount'] < 0:
                withdraw += record['amount']
        return abs(withdraw)

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

def create_spend_chart(categories):
    # get the total amount spent in all categories
    total_spent = sum([c.get_withdraw() for c in categories])
    # calculate the percentage spent in each category
    percentages = [round((c.get_withdraw() / total_spent) * 100) for c in categories]
    # round down the percentage to the nearest 10
    rounded_percentages = [p - (p % 10) for p in percentages]

    # create the chart header
    chart = "Percentage spent by category\n"
    # add the horizontal lines and categories
    for i in range(100, -10, -10):
        line = str(i).rjust(3) + "| "
        for p in rounded_percentages:
            if p >= i:
                line += "o  "
            else:
                line += "   "
        chart += line + "\n"

    # add the horizontal line below the bars
    chart += "    " + "-" * ((len(categories) * 3) + 1) + "\n"
    
    # find the longest category name
    nmax = 0
    for i in categories:
        if nmax < len(i.name):
            nmax = len(i.name)
    
    for letter_num in range(nmax):
        chart += "   "
        for c in categories:
            try:
                chart += "  " + c.name[letter_num]
            except:
                chart += "   "
        chart += "\n"

    return chart

