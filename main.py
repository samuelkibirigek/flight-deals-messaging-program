#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

# 1. I created a google sheet with the google account to which sheety account is registered
# 2. I created a project on sheety with the google sheet URL




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


