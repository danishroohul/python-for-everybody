# This example shows us how to extract latitude and longitude
# of the given location search with proper formatted address

# Import necessary libraries
import urllib.request, urllib.parse, urllib.error
import json

# Dr Chuck's website gives us access to google api by using the following details
api_key=42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# We dont use the url below because we dont have an api key
#serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    # Enter the address of your choice
    address = input("Enter Location: ")
    # If there is no address, exit the loop
    if len(address) < 1: break

    # Create a dictionary which has address and api key
    params = dict()
    params["address"] = address
    # Set the api key required by Dr Chuck's website
    if api_key is not False: params['key'] = api_key
    # urlencode creates the required url format for searching online
    url = serviceurl + urllib.parse.urlencode(params)
    print("Retrieving",url)
    # Access the data from the net using urlopen
    uh = urllib.request.urlopen(url)
    # Decode the data to bring it to readable format
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')

    # Try to convert the retrieved json into dictionary, else set it to None
    try:
        js = json.loads(data)
    except:
        js = None

    # If there is problem Retrieving, print the following
    if not js or 'status' not in js or js['status'] != 'OK':
        print("===== Failure to Retrieve =====")
        print(data)
        continue

    # Use this to see the retrieved json data
    #print(json.dumps(js, indent = 4))

    #Extracting proper formatted address of the given location
    place_id = js["results"][0]['place_id']
    print("Place id",place_id)
