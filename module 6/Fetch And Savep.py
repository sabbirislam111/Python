
# Download and set wallpaper

import requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# get the jeson
response = requests.get(api_url)
content = response.content.decode("UTF-8")

# convert the int to json
dict_content = json.loads(content)

# Get url
image_url = dict_content['url']

# Download image
dwn = requests.get(image_url)


# Save the image
with open('apod.png', 'wb') as image:
    image.write(dwn.content)

# ser wallpaper
PyWallpaper.change_wallpaper('E:\python\module 6\apod.png')