"""
Name: Max Oliver
traffic.py

Problem: calculates the average number of vehicles traveled down each road per day
as well as the total number of vehicles and the average number of vehicles for all of the roads.


Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    road_surv = eval(input("How many roads were surveyed?"))
    acc1 = 0
    for i in range(road_surv):
        days_surv = eval(input("How many days was road " + str(i+1) + " surveyed?"))
        acc2 = 0
        for _ in range(days_surv):
            cars_trav = eval(input("How many cars traveled on day " + str(_+1) + "?"))
            acc2 = acc2 + cars_trav
        print("Road " + str(i+1) + " average vehicles per day:", round(acc2 / days_surv, 2))
        acc1 = acc1 + acc2
    total_cars = acc1
    avgr = round(total_cars / road_surv, 2)
    print("Total number of vehicles traveled on all roads: ", total_cars)
    print("Average number of vehicles per road: ", avgr)


if __name__ == '__main__':
    main()
