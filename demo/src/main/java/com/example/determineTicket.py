import math
from datetime import datetime
import random
import csv

def distance(lat1, lon1, lat2, lon2):
    #Convert to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    #Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (math.sin(dlat/2)**2) + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2)**2)
    c = 2 * math.asin(math.sqrt(a))
    #Radius of earth in kilometers. Use 3959 for miles
    r = 6371
    return c * r

def ticket_price(distance, low, high, class_multiplier):
    price = int((distance*random.uniform(0.01, 0.15))*class_multiplier + random.uniform(low,high))
    while True:
        if class_multiplier == 1:
            return price
        elif class_multiplier == 5:
            if price > class_multiplier * ticket_price(distance, low, high, 1) and price < class_multiplier * ticket_price(distance, low, high, 1) * 1.2:
                return price
            else:
                price = int((distance*random.uniform(0.01, 0.15))*class_multiplier + random.uniform(low,high))
        elif class_multiplier == 8:
            if price > class_multiplier * ticket_price(distance, low, high, 1) and price < class_multiplier * ticket_price(distance, low, high, 1) * 1.1:
                return price
            else:
                price = int((distance*random.uniform(0.01, 0.15))*class_multiplier + random.uniform(low,high))

def cheapest_days(distance, departure_date, return_date):
    prices = {}
    economy_price = ticket_price(distance, 200, 1400, 1) + ticket_price(distance, 600, 1400, 1)
    business_price = ticket_price(distance, 700, 900, 5) + ticket_price(distance, 700, 900, 5)
    first_price = ticket_price(distance, 900, 1400, 8) + ticket_price(distance, 900, 1600, 8)
    prices[departure_date] = {"economy": economy_price, "business": business_price, "first": first_price}
    return prices

distance = int(input("What is the distance in kilometers between the two countries? "))
departure_date = input("What day do you want to depart in format YYYY-MM-DD? ")
return_date = input("What day do you want to return in format YYYY-MM-DD? ")

prices = cheapest_days(distance, departure_date, return_date)

with open('prices.csv', mode='w') as csv_file:
    fieldnames = ['Departure Date', 'Return Date', 'Class', 'Price', 'Cost to Go', 'Cost to Return', 'Total Cost']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for class_name, price in prices[departure_date].items():
        cost_to_go = int(price / 2)
        cost_to_return = int(price / 2)
        total_cost = price
        writer.writerow({'Departure Date': departure_date, 'Return Date': return_date, 'Class': class_name, 'Price': price, 'Cost to Go': cost_to_go, 'Cost to Return': cost_to_return, 'Total Cost': total_cost})
        print(f"{class_name}: {price}")
    print("Prices have been written to prices.csv.")
