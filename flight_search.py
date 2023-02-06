import requests
from pprint import pprint
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "beQ2TKPoZIHJ-JtOncQxGSCUWMQWPo1S"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}

        response = requests.get(url=location_endpoint, headers=headers, params=query)
        code = response.json()['locations'][0]['code']
        return code

