class Persone:
    def __init__(self, name, age, phone_number):
        assert len(phone_number) == 11, f'{len(phone_number)} digits is unvalid phone number '
        assert age > 13, f'you age is under 13 years old'
        self.name = name
        self.age = age
        self.phone_number = phone_number

sabbir = Persone("sabbir", 15, "0132420118")
print(sabbir)