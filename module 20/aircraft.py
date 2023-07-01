class Aircraft:
    def __init__(self, make, code, typ, flight_range):
        self.make = make
        self.code = code
        self.typ = typ
        self.flight_range = float(flight_range)
    
    def get_maek(self):
        return self.make
    
    def __repr__(self) -> str:
        return f'Make by : {self.make} code number : {self.code} type : {self.typ} flight range : {self.flight_range}'