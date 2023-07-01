
from random import random, randint, choice
import hashlib
from brta import BRTA
from vehicles import Bike, Car, Cng
from ride_manager import ubar
import threading

license_authurity = BRTA()

class Useralreadyexists(Exception):
    def __init__(self, email):
        print(f'{email} already exists')
      
  
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        file_list = []
        pwd_incrypted = hashlib.md5(password.encode()).hexdigest()
        allready_exists = False

        with open('user.txt', 'r') as file:
            if email in file.read():
                allready_exists = True
                raise Useralreadyexists(email)
        file.close()

        if allready_exists == False:
            with open('user.txt', 'a') as file:
                file.write(f'{email} {pwd_incrypted}\n')
            file.close()

    @staticmethod
    def log_in(email, password):
        stord_password = ''
        with open('user.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if email in line:
                    stord_password = line.split(' ')[1]
        file.close()
        # print("stord_password", stord_password)
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        if stord_password == hashed_pass:
            print("Valid password")
        else:
            print("Unvalid password")


class Rider(User):
    def __init__(self, name, email, password, location, balance):
        self.location = location
        self.balance = balance
        self.trip_info = []
        super().__init__(name, email, password)
        

    def set_location(self, location):
        self.location  = location

    def get_location(self):
        return self.location
    
    def requested_tripe(self):
        pass

    def start_a_tripe(self, fare, trip_info):
        self.balance -= fare
        self.trip_info.append(trip_info)


class Driver(User):
    def __init__(self, name, email, password, location, license):
        super().__init__(name, email, password)
        self.location  = location
        self.license = license
        self.validate_license = license_authurity.validate_license(email, license)
        self.earning = 0
        self.__trip_info = []
        self.vehicle = None

    def take_driving_test(self):
        result = license_authurity.take_driving_test(self.email)
        if result == False:
            # print("sorry you are failed")
            self.license = None
        else:
            self.license = result
            self.validate_license = True
            # print(f'{self.name} was created')

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.validate_license == True:
            if vehicle_type == 'car':
                self.vehicle = Car(vehicle_type, license_plate, rate, self)
                ubar.add_a_vehicaes(vehicle_type, self.vehicle)
            elif vehicle_type == 'bike':
                self.vehicle = Bike(vehicle_type, license_plate, rate, self)
                ubar.add_a_vehicaes(vehicle_type, self.vehicle)
            else:
               self.vehicle = Cng(vehicle_type, license_plate, rate, self)
               ubar.add_a_vehicaes(vehicle_type, self.vehicle) 
        else:
            # print("you are not a validate driver")
            pass


    def start_a_tripe(self, start, destinations, fare, trip_info):
        self.earning += fare
        self.location = destinations
        trip_thred = threading.Thread(target= self.vehicle.start_driving, args=(start, destinations,))
        trip_thred.start()
        self.__trip_info.append(trip_info)

    def get_trip_info(self):
        return self.__trip_info


sabbir = User("sabbir", "sabbirmollah302@gmail.com", "sabbiWFD234")

# User.log_in("sabbirmollah302@gmail.com", "sabbiWFD234")


rider1 = Rider('rider1', 'random1@gmail.com', ' rider1#4353', randint(1, 30), 5000)
rider2 = Rider('rider2', 'random2@gmail.com', ' rider2#4353', randint(1, 30), 5000)
rider3 = Rider('rider3', 'random3@gmail.com', ' rider3#4353', randint(1, 30), 5000)

choice_list = ['car', 'bike', 'cng']


for i in range(1, 100):
    driver1 = Driver(f'driver{i}', f'driver{i}@gmail.com', f'sdfjkf{i}42234', randint(1, 100), randint(10000, 99999))
    driver1.take_driving_test() 
    driver1.register_a_vehicle(choice(choice_list), f'2344{i}kh', randint(1, 50))
    driver1.register_a_vehicle(choice(choice_list), f'2344{i}kh', randint(1, 50))
    driver1.register_a_vehicle(choice(choice_list), f'2344{i}kh', randint(1, 50))
  

print(ubar.get_available_cars())
ubar.find_a_vahicle(rider1, choice(choice_list), randint(1, 100))
ubar.find_a_vahicle(rider2, choice(choice_list), randint(1, 100))
ubar.find_a_vahicle(rider3, choice(choice_list), randint(1, 100))




