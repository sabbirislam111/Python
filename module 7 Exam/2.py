import requests
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()

api_key = '783b944082d0aeb5eed2f939b256a628'

user_input = "Dhaka"

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

def get_weather():
    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        celsius = int((temp - 32) / 1.8)
        # print(f"The weather in {user_input} is: {weather}")
        # print(f"The temperature in {user_input} is: {temp}ºF")
        while 1:
            toaster.show_toast("weather in Dhaka!",
                        f"The weather in {user_input} is: {weather} \nThe temperature in {user_input} is: {celsius}ºC",
                        icon_path = None,
                        duration=5,
                        threaded=True
                        )

            # Wait for threaded notification to finish
            while toaster.notification_active(): time.sleep(30.00) 

get_weather()