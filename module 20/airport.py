class Airport:
    def __init__(self, name, city, country, lat, lon, rate):
        # self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.lon = float(lon)
        self.rate = float(rate)
    
    def __repr__(self) -> str:
        return f'Airport : {self.name} Country : {self.country} Latitude : {self.lat} Longitude : {self.lon} Rate : {self.rate} '