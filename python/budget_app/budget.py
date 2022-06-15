class Category:
    # initialize all
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, budget_category):
        if not self.withdraw(amount, "Transfer to " + budget_category.category):
            return False

        budget_category.deposit(amount, "Transfer from " + self.category)
        return True

    def __str__(self):
        st = self.category.center(30, "*") + "\n"

        for item in self.ledger:
            temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
            st += temp + "\n"

        st += "Total: " + str(self.get_balance())
        return st


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  s = "Percentage spent by category"
  for i in range(100, -1, -10):
    s += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s += " o "
      else:
        s += "   "

    s += " "
  s += "\n    ----------"

  cat_length = []
  for category in categories:
    cat_length.append(len(category.category))
  max_length = max(cat_length)

  for i in range(max_length):
    s += "\n    "
    for j in range(len(categories)):
      if i < cat_length[j]:
        s += " " + categories[j].category[i] + " "
      else:
        s += "   "

    s += " "

  return s