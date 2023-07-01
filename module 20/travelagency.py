from all_airports import Allairports
from airlince import Airlince
from trip import Trip
from itertools import permutations

class Travelagency:
    def __init__(self, name):
        self.name = name
        self.trips = None
        self.allairports = Allairports()
        self.airlince = Airlince()
        

    def set_trip_one_city_one_way(self, start, end, start_date):
        price = self.allairports.get_ticket_price(start, end)
        distance = self.allairports.distace_between_two_airport(start, end)
        aircraft = self.airlince.get_aircraft_by_distance(distance)
        trip = Trip([start, end],start_date,aircraft,price,[start,end])

        return trip
  

    def set_trip_one_city_round_way(self, start, end, start_date):
        trip1 = self.set_trip_one_city_one_way(start, end, start_date)
        trip2 = self.set_trip_one_city_one_way(end, start, start_date)
        return [trip1, trip2]


    def set_trip_two_city_one_way(self, trip_info, start_date):
        trip1 = self.set_trip_one_city_one_way(trip_info[0], trip_info[1], start_date)
        trip2 = self.set_trip_one_city_one_way(trip_info[1], trip_info[2], start_date)
        return [trip1, trip2]


    def set_trip_multi_city_one_way_fixed_route(self, trip_info, start_date):
        trips = []
        for i in range(0, len(trip_info)-1):
            trip = self.set_trip_one_city_one_way(trip_info[i], trip_info[i + 1], start_date)
            trips.append(trip)
        return trips

    
    def set_trip_multi_city_flexible_way(self, trip_info, start_date):
        strt_city = trip_info[0]
        flexible_city = trip_info[1:]
        min_price = float('inf') 
        select_trip =  None

        for sequence in permutations(flexible_city):
            # print(sequence)
            fixd_rute = [strt_city] + list(sequence)
            fixd_rute_trip = self.set_trip_multi_city_one_way_fixed_route(fixd_rute, start_date)
            price = 0
            for trip in fixd_rute_trip:
                price += trip.price
            if price < min_price:
                min_price = price
                select_trip = fixd_rute_trip
        return select_trip, min_price


    def __repr__(self) -> str:
        return f'Name : {self.name}'
