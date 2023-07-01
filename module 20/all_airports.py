import csv
from airport import Airport
import math
class Allairports:
    def __init__(self):
        self.airports = None
        self.load_airports_data("./data/airport.csv")

    def load_airports_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}
         
        # get currency name <-----> rate
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()

        # country_name <-----> currency
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)
            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()

        # create airport
        with open(file_path, 'r', encoding= 'utf8') as file:
            lines = csv.reader(file)

            # handle KeyError
            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport( line[1],line[2],line[3], line[6], line[7], rate)
            except KeyError as e:
                print(e)

            self.airports = airports

            # for airport in self.airports.items():
            #     print(airport)

    def get_distance_between_airports(self, lat1, lon1, lat2, lon2):
        # its a formula
        radius = 6371  # km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
            math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c
        return d

    def distace_between_two_airport(self, airport1_code, airport2_code):
        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_between_airports(airport1.lat, airport1.lon, airport2.lat, airport2.lon)
        return distance

    def get_ticket_price(self, start, end):
        distance = self.distace_between_two_airport(start,end)
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare

    

 


world_tour =Allairports()
fare = world_tour.get_ticket_price('TII', 'PRA')
print('Ticket pare :', fare)

