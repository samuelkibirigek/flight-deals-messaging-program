import requests
#used pprint to format output
# from pprint import pprint


# created a class
class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.iata_code = {
            "price": {
                "iataCode": "TESTING"
            }
        }

    def s_data(self):
        # 3. Used sheety API to checkout the data and connection btn sheety and google sheet
        self.sheets_endpoint = "https://api.sheety.co/198d9027ea41ea054b7525a9a3b7029b/kibirigeFlightDeals/prices"
        get_response = requests.get(url=self.sheets_endpoint)
        # pprint(get_response.json())
        return get_response.json()['prices']

    def update_data(self, the_sheet):
        #6. went ahead to actually update the google sheet iataCode column to have TESTING
        put_partial_endpoint = "https://api.sheety.co/198d9027ea41ea054b7525a9a3b7029b/kibirigeFlightDeals/prices/"
        for city in the_sheet:
            requests.put(url=f"{put_partial_endpoint}{city['id']}", json=self.iata_code)


