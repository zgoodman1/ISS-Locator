import json
import urllib.request
import turtle

# creates a variable that stores a url to a web service that displays ISS astronauts and their locations
url_people = 'http://api.open-notify.org/astros.json'

# calls the web service and saves the JSON data as response
json_ppl_data = urllib.request.urlopen(url_people)

# translates the JSON data to a Python data structure
ppl_in_space = json.loads(json_ppl_data.read())

people = ppl_in_space['people']

# print(ppl_in_space['number'], 'people in space')
#
# for p in people:
#     print(p['name'], 'in ', p['craft'])

url_iss = 'http://api.open-notify.org/iss-now.json'

json_iss_data = urllib.request.urlopen(url_iss)

iss_location = json.loads(json_iss_data.read())

location = iss_location['iss_position']
lon = location['longitude']
lat = location['latitude']

# creates a turtle object, same as tkinter's windows
screen = turtle.Screen()

# sets the size of the window in pixels
screen.setup(1000, 610)

# coordinates for the map of the world being used as the image,
# starts as bottom left (x, y) and then top right (x, y)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

# registers a turtle object similar to a drawing/shape
screen.register_shape('iss_astro2.gif')
iss = turtle.Turtle()
iss.shape('iss_astro2.gif')
iss.setheading(90)

# same as tkinter's root.mainloop()
turtle.done()
