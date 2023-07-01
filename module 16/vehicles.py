from abc import ABC, abstractclassmethod
from time import sleep


class Vehicle(ABC):
    speed = {
        'car' : 30,
        'bike' : 50,
        'cng' : 20,
    }

    def __init__(self, vehicle_type, license_plate, rate, driver):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.statars = 'available'
        self.driver = driver
        self.speed = self.speed[self.vehicle_type]

    @abstractclassmethod
    def start_driving():
        pass

    @abstractclassmethod
    def trip_finished():
        pass
    

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
       super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.statars = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(1)
            print(f'driveing {self.license_plate} current position {i} to {destination}')
        self.trip_finished()


    def trip_finished(self):
        self.statars = 'available'
        print(self.vehicle_type, self.license_plate, 'Finished tripe')



class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
       super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.statars = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(1)
            print(f'driveing {self.license_plate} current position {i} to {destination}')
        self.trip_finished()


    def trip_finished(self):
        self.statars = 'available'
        print(self.vehicle_type, self.license_plate, 'Finished tripe')



class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver):
       super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self, start, destination):
        self.statars = 'unavailable'
        print(self.vehicle_type, self.license_plate, 'Started')
        distance = abs(start - destination)
        for i in range(0, distance):
            sleep(0.2)
            print(f'driveing {self.license_plate} current position {i} to {destination}')
        self.trip_finished()


    def trip_finished(self):
        self.statars = 'available'
        print(self.vehicle_type, self.license_plate, 'Finished tripe')
    