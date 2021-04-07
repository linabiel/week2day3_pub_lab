import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100)
        self.customer = Customer("Gordon", 100, 25)
        self.customer_2 = Customer("Lina", 100, 17)
        self.drink = Drink("Tennents Lager", 5, 10)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_can_refuse_service(self):
        self.customer.customer_buys_drink(self.drink)
        self.customer.customer_buys_drink(self.drink)
        self.customer.customer_buys_drink(self.drink)
        self.assertEqual(True, self.customer.drunkeness)
