import json
import turtle
import urllib.request

# creates a variable that stores a url to a web service that displays ISS astronauts and their locations
url = 'http://api.open-notify.org/astros.json'

# calls the web service and saves the JSON data called as response
response = urllib.request.urlopen(url)

# translates the JSON data to a Python data structure
result = json.loads(response.read())

print(result)