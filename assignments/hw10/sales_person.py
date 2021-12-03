"""

Name: Max Oliver
sales_person.py

Problem: make a class that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, id, name):
        self.employee_id = id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = sum(self.sales)
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        else:
            return False

    def compare_to_other(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        if self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ": " + str(self.total_sales())
