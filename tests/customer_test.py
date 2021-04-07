import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Gordon", 100)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Tennents Lager", 5)

    def test_customer_has_name(self):
        self.assertEqual("Gordon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        self.pub.add_money_to_till(self.drink.price)
        self.assertEqual(105, self.pub.till)
