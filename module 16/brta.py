
import random

class BRTA:
    def __init__(self):
        self.__license = {}

    def take_driving_test(self, email):
        score = random.randint(1, 100)
        if score >= 33:
            # print(f"welcome, you are passed {score}")
            license_number = random.randint(5000, 9999)
            # print(license_number)
            self.__license[email] = license_number
            return license_number

        else:
            # print("sorry, you are failed")
            return False

    def validate_license(self, email, license):
        for key, value in self.__license.items():
            if key == email and value == license:
                return True
        return False


        



