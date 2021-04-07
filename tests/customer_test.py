import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Gordon", 100)

    def test_customer_has_name(self):
        self.assertEqual("Gordon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100, self.customer.wallet)
