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
    return int((distance*random.uniform(0.01, 0.15))*class_multiplier + random.uniform(low,high))

def cheapest_days(distance, month, days):
    prices = {}
    days_in_month = 31 if month in [1,3,5,7,8,10,12] else 30
    for i in range(1,days_in_month+1):
        if i % 7 == 0 or i % 7 == 6 :
            prices[i] = {"economy": ticket_price(distance, 200, 600, 1), "business": ticket_price(distance, 400, 600, 5), "first": ticket_price(distance, 700, 1100, 7)}
        else:
            prices[i] = {"economy": ticket_price(distance, 600, 1400, 1), "business": ticket_price(distance, 700, 900, 5), "first": ticket_price(distance, 900, 1100, 8)}
    min_price = float('inf')
    for day, price in prices.items():
        return_day = (day + days - 1) % days_in_month + 1
        if (day + days - 1) > days_in_month:
            return_month = (month % 12) + 1
        else:
            return_month = month
        economy_price = prices[day]["economy"] + prices[return_day]["economy"]
        business_price = prices[day]["business"] + prices[return_day]["business"]
        first_price = prices[day]["first"] + prices[return_day]["first"]
        if economy_price < min_price:
            min_price = economy_price
            cheapest_class = "economy"
            cheapest_departure_day, cheapest_return_day, cheapest_return_month = day, return_day, return_month
        if business_price < min_price:
            min_price = business_price
            cheapest_class = "business"
            cheapest_departure_day, cheapest_return_day, cheapest_return_month = day, return_day, return_month
        if first_price < min_price:
            min_price = first_price
            cheapest_class = "first"
            cheapest_departure_day, cheapest_return_day, cheapest_return_month = day, return_day, return_month
    return cheapest_departure_day, cheapest_return_day, cheapest_return_month, prices, cheapest_class

distance = int(input("What is the distance in kilometers between the two countries? "))
month = int(input("What month would you like to travel in? "))
days = int(input("How many days do you want to stay? "))

# Handle case where user enters a month greater than 12
if month > 12:
    month = month % 12

min_total_price = float('inf')
best_month = month
cheapest_class = ""
for i in range(12):
    departure_day, return_day, return_month, prices, class_price = cheapest_days(distance, month, days)
    if prices[departure_day][class_price] + prices[return_day][class_price] < min_total_price:
        min_total_price = prices[departure_day][class_price] + prices[return_day][class_price]
        cheapest_departure_day, cheapest_return_day, cheapest_return_month, cheapest_class = departure_day, return_day, return_month, class_price
        best_month = month
    month = (month % 12) + 1

departure_date = datetime.strftime(datetime(2023, best_month, cheapest_departure_day), '%Y-%m-%d')
return_date = datetime.strftime(datetime(2023, cheapest_return_month, cheapest_return_day), '%Y-%m-%d')

print("The cheapest option to travel is: " )
print("Departure Date: " + departure_date)
print("Departure Ticket Cost (economy, business, first): " + str(prices[cheapest_departure_day]["economy"]) + ", " + str(prices[cheapest_departure_day]["business"]) + ", " + str(prices[cheapest_departure_day]["first"]))
print("Return Date: " + return_date)
print("Return Ticket Cost (economy, business, first): " + str(prices[cheapest_return_day]["economy"]) + ", " + str(prices[cheapest_return_day]["business"]) + ", " + str(prices[cheapest_return_day]["first"]))
print("Total Ticket Cost (economy, business, first): " + str(prices[cheapest_departure_day]["economy"] + prices[cheapest_return_day]["economy"]) + ", " + str(prices[cheapest_departure_day]["business"] + prices[cheapest_return_day]["business"]) + ", " + str(prices[cheapest_departure_day]["first"] + prices[cheapest_return_day]["first"]))
with open("flight_prices.csv", mode="w") as csv_file:
        fieldnames = ["Departure Date", "Arrival Date", "Class","Departure Price", "Arrival Price","Total Price"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for class_name in prices[cheapest_departure_day]:
            writer.writerow({"Departure Date": departure_date,
                             "Arrival Date": return_date,
                             "Class": class_name,
                             "Departure Price": prices[cheapest_departure_day][class_name],
                             "Arrival Price": prices[cheapest_return_day][class_name],
                             "Total Price": prices[cheapest_departure_day][class_name] + prices[cheapest_return_day][class_name]
                            })

#last thing, take this code, add functions to make it clean. Make sure that ou keep the functionalities. Everytime i ask you you remove the datetime and change the cod eup. Don't do that, just break the code into functions and add doc strings
