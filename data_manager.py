import requests
from flight_search import FlightSearch
# used pprint to format output
# from pprint import pprint

sheets_endpoint = "https://api.sheety.co/198d9027ea41ea054b7525a9a3b7029b/kibirigeFlightDeals/prices"

# created a class
class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # Update iataCode to be empty again as we prepare to enter real data
        pass

    def s_data(self):
        # 3. Used sheety API to checkout the data and connection btn sheety and google sheet
        get_response = requests.get(url=sheets_endpoint)
        # pprint(get_response.json())
        return get_response.json()['prices']

    def update_data(self, the_sheet):
        # 6. went ahead to actually update the google sheet iataCode column to have TESTING
        for row in the_sheet:
            search = FlightSearch()
            # 7.
            code = search.get_destination_code(row['city'])
            iata_code = {
                "price": {
                    "iataCode": code
                }
            }
            requests.put(url=f"{sheets_endpoint}/{row['id']}", json=iata_code)


