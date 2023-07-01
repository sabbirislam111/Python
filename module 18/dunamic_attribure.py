
class User:
    all = []

    def __init__(self, name, addresh):
        self.__name = name
        self.__addersh = addresh
        self.all.append(self)

    def __repr__(self) -> str:
        return f"{self.name} {self.addersh}"
    

    
sabbir = User("Sabbir", "Gopalginj")
sadia = User("sadia", "Khulna")
sabbir._User__name = "salman"

print(sabbir._User__name)

