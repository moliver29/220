"""
Name: Max Oliver
sales_force.py

Problem: make a class that encapsulates data for a sales person

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        data = infile.read().split(",")
        self.sales_people.append(data)

    def quota_report(self, quota):
        

    def top_seller(self):

    def individual_sales(self, employee_id):
