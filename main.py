#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# 1. I created a google sheet with the google account to which sheety account is registered
# 2. I created a project on sheety with the google sheet URL

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import requests

data = DataManager()
# 4. stored the data in sheet_data variable using a method in DataManager class from data_manager file/module
sheet_data = data.s_data()
search = FlightSearch()
# print(sheet_data)

# 5. checking if sheet_data column iataCode is empty and filling it with word TESTING
# for city in sheet_data:
#     search.codes(city)
#
#print(sheet_data)

data.update_data(sheet_data)

ORIGIN_CITY_IATA = "LON"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )





