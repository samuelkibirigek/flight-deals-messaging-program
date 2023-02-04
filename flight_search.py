class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def codes(self, city_name):
        if city_name['iataCode'] == "":
            city_name['iataCode'] = "TESTING"



