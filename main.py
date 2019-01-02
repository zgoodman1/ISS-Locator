import json
import urllib.request
import turtle
import time

# creates a variable that stores a url to a web service that displays ISS astronauts and their locations
people_url = 'http://api.open-notify.org/astros.json'

# calls the web service and saves the JSON data as response
json_ppl_data = urllib.request.urlopen(people_url)

# translates the JSON data to a Python data structure
ppl_in_space = json.loads(json_ppl_data.read())

people = ppl_in_space['people']

# print(ppl_in_space['number'], 'people in space')
#
# for p in people:
#     print(p['name'], 'in ', p['craft'])

iss_url = 'http://api.open-notify.org/iss-now.json'

json_iss_data = urllib.request.urlopen(iss_url)

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

# moves the astronaut picture/ISS location to the latitude and longitude
iss.penup()
iss.goto(float(lon), float(lat))
# iss.write('Lat: ' + lat + ' Lon: ' + lon, True, font=('Arial', 12, 'bold'))

# latitude and longitude for the space center in Houston, Texas
# *** not actual coordinates, had to tweak numbers to fit in the
# picture that was used ***
lat_h = 11.5502
lon_h = -91.097

# making a new turtle object to represent Houston with a dot
houston = turtle.Turtle()
houston.penup()
houston.color('yellow')
houston.goto(lon_h, lat_h)
houston.dot(5)
houston.hideturtle()

# finds the next pass of the ISS over Houston
houston_url = 'http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1'
houston_json = urllib.request.urlopen(houston_url)
houston_next = json.loads(houston_json.read())
houston_pass = houston_next['response'][1]['risetime']

# writes the next time the ISS will be above Houston using the ctime function
# (our time + seconds)
houston.write(time.ctime(houston_pass), font=('Arial', 14, 'bold'))

# same as tkinter's root.mainloop()
turtle.done()
