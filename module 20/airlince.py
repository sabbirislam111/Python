import csv
from aircraft import Aircraft
class Airlince:
    def __init__(self):
        self.air_craft = None
        self.lod_air_craft_data("./data/aircraft.csv")
        
    def lod_air_craft_data(self, cav_file):
        air_craft = {}
        with open(cav_file, 'r') as file:
            lines = csv.reader(file)
            next(lines)
            for line in lines:
                air_craft[line[0]] = Aircraft(line[3], line[0], line[1], line[4])
        file.close()
        self.air_craft = air_craft

        # for air in air_craft.items():
        #     print(air)
    
    def get_aircraft(self, aircraft_cod):
        return self.air_craft[aircraft_cod]

    def get_aircraft_by_distance(self, distance):
        for airCraft in self.air_craft.values():
            if airCraft.flight_range < distance:
                return airCraft
        

a = Airlince()

