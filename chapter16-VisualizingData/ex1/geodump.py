# This code is used to create visualization on google maps based
# on location data in database

# Import required libraries
import sqlite3
import json
import codecs

# Set up a connection and cursor for the database
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# Extract all rows and columns from database
cur.execute('SELECT * FROM Locations')

# open javascript file in write mode
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

# Loop for every row in database
for row in cur :
    data = str(row[1].decode())
    # Try to load the data or continue if there are any exceptions
    try: js = json.loads(str(data))
    except: continue

    # If status in json is not OK, dont proceed
    if not('status' in js and js['status'] == 'OK') : continue

    # Extract latitude and longitude data from json
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue

    # Extract formatted address from json
    where = js['results'][0]['formatted_address']
    # Make address look cleaner
    where = where.replace("'", "")

    # Try writing address in javascript file
    try :
        print(where, lat, lng)
        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

# Close all files and connections
fhand.write("\n];\n")
cur.close()
fhand.close()

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
