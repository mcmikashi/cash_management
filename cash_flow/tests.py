from django.test import TestCase
from .models import Category, Transaction
from decimal import Decimal
from datetime import date as dt
class CategoryTestCase(TestCase):

    def setUp(self):
        self.category_1 = Category.objects.create(label="Sales")

    def test_str(self):
        """ Testtthe str fucntion of the Category model """
        self.assertEqual(self.category_1.__str__(),"Sales")

    def test_data(self):
        """ Test the data field of the Category model """
        self.assertEqual(self.category_1.label,"Sales")

class TransactionTestCase(TestCase):

    def setUp(self):
        self.category_data = {
            'label': 'Computer sales',
            'tax': Decimal(20.00),
            'amount': Decimal(1000.00),
            'date': dt.today(),
        }
        self.including_tax = round(self.category_data["amount"] + (self.category_data["amount"] * (self.category_data["tax"] / 100 )),2)
        self.category = Category.objects.create(label="Sales")
        self.transaction_1 = Transaction.objects.create(
            label=self.category_data['label'],
            amount=self.category_data['amount'],
            tax=self.category_data['tax'],
            date=self.category_data['date'])
    
    def test_str(self):
        """ Test the str fucntion of the Transaction model """
        self.assertEqual( self.transaction_1.__str__(),f"{self.category_data['label']} - {self.including_tax} - {self.category_data['date']}")

    def test_data(self):
        """ Test the data field of the category model """
        self.assertEqual(self.transaction_1.label, self.category_data["label"])
        self.assertEqual(self.transaction_1.amount, self.category_data["amount"])
        self.assertEqual(self.transaction_1.tax, self.category_data["tax"])
        self.assertEqual(self.transaction_1.date, self.category_data["date"])
        self.assertEqual(self.transaction_1.including_tax, self.including_tax)
