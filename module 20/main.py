from travelagency import Travelagency
from all_airports import Allairports

def main():
    travel_agent = Travelagency("sah jalal")
    trip_info1 = travel_agent.set_trip_one_city_one_way('TII', 'TEE', '05/3/2023')
    # print("Aircraft ",trip_info1.aircrafts)
    # print("Price ", trip_info1.price)

    # all_airports = Allairports()
    # all_airports.get_ticket_price('TII', 'TEE')

    trip_citys = ['TEE', 'QAS', 'ORN', 'LOO']
    trip_info = travel_agent.set_trip_multi_city_flexible_way(trip_citys, '05/3/2023')
    print("price :", trip_info[1])

    for trip in trip_info[0]:
        print(trip)



if __name__ == '__main__':
   main()
    