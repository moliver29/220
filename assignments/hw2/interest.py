"""
Name: Max Oliver
Interest.py

Problem: Calculates the monthly interest rate based on the average daily balance of an account

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def main():
        interest = eval(input("Enter the annual interest rate:"))  # acquire the annual interest rate
        cycle = eval(input("Enter the number of days in the billing cycle:"))  # acquire the number of days in the month
        netBalance = eval(input("Enter the previous net balance"))  # Acquire the net balance of the account
        payment = eval(input("Enter the amount of the payment that was made:"))  # Acquire the amount of money for the payment
        day = eval(input("Enter the day of the billing cycle that the payment was made:"))  # Acquire the day that the payment was made
        daysBeforeEnd = cycle-day
        result1 = netBalance*cycle
        result2 = payment*daysBeforeEnd
        result3 = result1-result2
        avgDaily = result3/cycle
        monthlyIntRate = (interest/12)/100
        monthlyIntCharge = avgDaily*monthlyIntRate
        print(round(monthlyIntCharge, 2))


if __name__ == "__main__":
        main()
