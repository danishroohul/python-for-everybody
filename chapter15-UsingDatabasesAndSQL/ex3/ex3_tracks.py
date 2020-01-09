# Import necessary modules
import xml.etree.ElementTree as ET
import sqlite3

# Create a connection to database with its cursor
conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

# Delete tables if they already exist
cur.execute("DROP TABLE IF EXISTS ARTIST")
cur.execute("DROP TABLE IF EXISTS ALBUM")
cur.execute("DROP TABLE IF EXISTS TRACK")

# Create table Artist
cur.execute('''
CREATE TABLE ARTIST (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    NAME TEXT UNIQUE
)
''')

# Create table Album
cur.execute('''
CREATE TABLE ALBUM (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    ARTIST_ID INTEGER,
    TITLE TEXT UNIQUE
)
''')

# Create table Track
cur.execute('''
CREATE TABLE TRACK (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    TITLE TEXT UNIQUE,
    ALBUM_ID INTEGER,
    LEN INTEGER,
    RATING INTEGER,
    COUNT INTEGER
)
''')

# Select an XML file to extract the tracks data from
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'Library.xml'

# Function to extract track details from XML
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

# extracts xml as ElementTree and saves it in stuff
stuff = ET.parse(fname)
# find all branches of the form dict/dict/dict (Find all tracks)
all = stuff.findall('dict/dict/dict')
#Count the number of tracks
print('Dict count:',len(all))
# Loop through all tracks information to extract individual details
for entry in all:
    # Skip the branch which doesn't have Track ID
    if lookup(entry, 'Track ID') is None: continue

    # Extract the following details of the track
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # If there is no information of the track, continue
    if name is None or artist is None or album is None: continue

    print(name, artist, album, count, rating, length)

    # Enter name of the artist of track into artist table
    cur.execute('''
    INSERT OR IGNORE INTO ARTIST(NAME) VALUES (?)
    ''', (artist,))

    # Fetch id of the artist and save it in artist_id
    cur.execute('''
    SELECT ID FROM ARTIST WHERE NAME = ?
    ''', (artist,))
    artist_id = cur.fetchone()[0]

    # Enter album name with artist ID
    cur.execute('''
    INSERT OR IGNORE INTO ALBUM( TITLE, ARTIST_ID) VALUES (?,?)
    ''', (album, artist_id))

    # Fetch album id and save it in album_id
    cur.execute('''
    SELECT ID FROM ALBUM WHERE TITLE = ?
    ''', (album,))
    album_id = cur.fetchone()[0]

    # Enter track information in track table if it doesnt exist
    cur.execute('''
    INSERT OR REPLACE INTO TRACK (TITLE, ALBUM_ID, LEN, RATING, COUNT)
    VALUES (?,?,?,?,?)
    ''', (name, album_id, length, rating, count) )

    conn.commit()

conn.close()
