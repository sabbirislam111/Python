
from tracemalloc import start
from turtle import distance


class Ridemanager:
    def __init__(self):
        print("Ride manager Acctivate")
        self.__income = 0
        self.__available_car = []
        self.__available_bike = []
        self.__available_cng = []
        self.__tripe_history = []

    def add_a_vehicaes(self,vehicle_type, vehicle):
        if vehicle_type == 'car':
            self.__available_car.append(vehicle)

        elif vehicle_type == 'bike':
            self.__available_bike.append(vehicle)

        elif vehicle_type == 'cng':
            self.__available_cng.append(vehicle)

    def get_available_cars(self):
        return self.__available_car

    def total_income(self):
        return self.__income

    def tripi_history(self):
        return self.__tripe_history


    def find_a_vahicle(self, rider, vehicle_type, destination):
        if vehicle_type == 'car':
            vehicles = self.__available_car
        elif vehicle_type == 'bike':
            vehicles = self.__available_bike
        elif vehicle_type == 'cng':
            vehicles = self.__available_cng


        if len(vehicles) == '0':
            print("sorry no care is available")
        for vehicle in vehicles:
            # print('potential', rider.location, car.driver.location)
            if abs(rider.location - vehicle.driver.location) <= 10:
                distance = abs(destination - rider.location)
                fare = distance * vehicle.rate
                if rider.balance < fare:
                    print("You don't have enough balance for this ride", fare)
                    return False
                if vehicle.statars == 'available':
                    vehicle.statars = 'unavailable'
                    vehicles.remove(vehicle)
                    trip_history = f"match for {rider.name} for fare {fare}, with {vehicle.driver.name}, start from {rider.location} to {destination}"
                    self.__tripe_history.append(trip_history)
                    rider.start_a_tripe(fare, trip_history)
                    vehicle.driver.start_a_tripe(rider.location , destination, fare, trip_history)
                    self.__income += fare*0.2
                    print(trip_history)
                    return True



ubar = Ridemanager()
