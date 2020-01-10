# This code is used to extract data and save it in database

# Import required libraries
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# Use the url and api_key given by Dr Chuck
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

# Set up a connection and cursor for the database
conn = sqlite3.connect("geodata.sqlite")
cur = conn.cursor()

# Create a table named LOCATIONS
cur.execute('''
CREATE TABLE IF NOT EXISTS LOCATIONS (ADDRESS TEXT, GEODATA TEXT)
''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open the data file
fh = open("where.data")
count = 0
for line in fh:
    # If count exceeds 200, quit
    if count > 200:
        print("Retrieved 200 locations, restart to retrieve more")
        break

    # Save address in a list
    address = line.strip()
    print('')
    # Extract the row from database with the above address
    cur.execute('''
    SELECT GEODATA FROM LOCATIONS WHERE ADDRESS = ?
    ''', (memoryview(address.encode()),))

    # If address found, skip the address, dont add
    try:
        data = cur.fetchone()[0]
        print("Found in database",address)
        continue
    # If not found, proceed with the code
    except:
        pass

    # Create a dictionary with the address and api_key
    params = dict()
    params["address"] = address
    if api_key is not False: params['key'] = api_key
    # Create the url with Dr Chuck's url, his api_key and address
    url = serviceurl + urllib.parse.urlencode(params)

    print("Retrieving", url)
    # Request the url and save the data in uh variable
    uh = urllib.request.urlopen(url, context = ctx)
    # Decode the data to convert it from utf-8 to string
    data = uh.read().decode()
    print("Retrieved", len(data), "characters", data[:20].replace('\n',' '))
    count = count + 1

    # If data retrieved, convert the string data into json format
    try:
        js = json.loads(data)
    except:
        print(data)
        continue

    # If the received data has problem, if status isnt OK, dont proceed
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print("===== Failure To Retrieve =====")
        print(data)
        break

    # Add the address text and the data retrieved into the database
    cur.execute('''
    INSERT INTO LOCATIONS (ADDRESS, GEODATA) VALUES(?,?)
    ''', (memoryview(address.encode()),memoryview(data.encode())))
    conn.commit()

    # Give some delay after 100 entries
    if count % 100 == 0:
        print("Pausing for a bit...")
        time.sleep(1)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
