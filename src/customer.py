class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def add_money_to_wallet(self, amount):
        self.wallet += amount

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def customer_buys_drink(self, drink):
        self.remove_money_from_wallet(drink.price)
        pub.add_money_to_till(drink.price)
