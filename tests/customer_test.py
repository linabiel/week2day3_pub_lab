import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Gordon", 100, 25)
        self.customer_2 = Customer("Lina", 100, 17)
        self.pub = Pub("The Prancing Pony", 100)
        self.drink = Drink("Tennents Lager", 5, 10)

    def test_customer_has_name(self):
        self.assertEqual("Gordon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_can_buy_drink(self):
        self.customer.customer_buys_drink(self.drink, self.pub)
        self.assertEqual(95, self.customer.wallet)
        self.assertEqual(105, self.pub.till)

    def test_customer_over_18(self):
        self.assertEqual(True, self.pub.check_customer_age(self.customer.age))

    def test_customer_under_18(self):
        self.assertEqual(
            False, self.pub.check_customer_age(self.customer_2.age))
