class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money_to_till(self, amount):
        self.till += amount

    def check_customer_age(self, age):
        if age >= 18:
            return True
        return False
