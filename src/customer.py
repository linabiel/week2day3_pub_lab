class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def add_money_to_wallet(self, amount):
        self.wallet += amount

    def remove_money_from_wallet(self, amount):
        self.wallet -= amount

    def customer_buys_drink(self, drink, pub, alcohol_level, refuse_service):
        if refuse_service == True:
            return None
        self.remove_money_from_wallet(drink.price)
        pub.add_money_to_till(drink.price)
        self.drunkeness += alcohol_level
