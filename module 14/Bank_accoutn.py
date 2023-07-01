
from cgi import print_arguments


class Accout:
    acNo = 1

    def __init__(self, name, nid, balance):
        self.name = name
        self.balance = balance
        self.nid = nid

        # update accout
        self.acNo = Accout.acNo
        Accout.acNo += 1


sabbir = Accout("Sabbir", 85023498723, 1000)
sadia = Accout("Sadia", 867563498723, 2000)

print(sabbir.acNo)
print(sadia.acNo)
        