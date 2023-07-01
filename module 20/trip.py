class Trip:
    def __init__(self, trip_citis, start_date, aircrafts, price, rute = ''):
        self.trip_citis = trip_citis
        self.start_date = start_date
        self.aircrafts = aircrafts
        self.price = price
        self.rute = rute
       


    def __repr__(self) -> str:
        # return f"Trip : {self.trip_citis} Aircrapts : {self.aircrafts} Start date : {self.start_date} rute : {self.rute} Cost : {self.price}"
        return f"Trip : {self.trip_citis} Cost : {self.price}"

    