# geocoding example with third party package
# from geopy import geocoders
#
# g = geocoders.GoogleV3()
# place, (lat, lng) = g.geocode("Olimpijska 26, sarajevo")
# print("{} {} {}".format(place, lat, lng))
#

# more info https://developers.google.com/places/web-service/search

from urllib.request import urlopen # this package is needed just to download data from web location
import json # this package we will use to easier decode json

response = urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
                                  "location=43.855624,18.379420" # your location in lat long coordinates
                                  "&radius=500" # radius in meters around coordinates to include in search
                                  "&types=food" # type of venue, try with cafe, bank etc.
                                  # "&name=slatko" # include for filtering by name
                                  "&key=AIzaSyBIde_4tmXK7iajeV2eMCMcREwTKaboWNE") # key for identification, create your own

jsonRaw = response.read().decode('utf-8') # this will read json from downloaded object
jsonData = json.loads(jsonRaw)  # this will convert json into python object

results = ','.join([result['name'] for result in jsonData['results']]) #ja dodao samo da ispiltriram nazive

print('Rezultati: {}'.format(results))

#################### points of interest
response = urlopen("https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
                                  "location=43.855624,18.379420" # your location in lat long coordinates
                                  "&radius=500" # radius in meters around coordinates to include in search
                                  "&types=bank" # type of venue, try with cafe, bank etc.
                                  # "&name=slatko" # include for filtering by name
                                  "&key=AIzaSyBIde_4tmXK7iajeV2eMCMcREwTKaboWNE") # key for identification, create your own
jsonRaw = response.read().decode('utf-8')
jsonData = json.loads(jsonRaw)
results = [result['name'] for result in jsonData['results']]

print('Results:  {}'.format(results))