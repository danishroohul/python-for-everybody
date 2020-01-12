import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create a connection to the database with its cursor
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Create a table Pages
cur.execute('''CREATE TABLE IF NOT EXISTS Pages
    (id INTEGER PRIMARY KEY, url TEXT UNIQUE, html TEXT,
     error INTEGER, old_rank REAL, new_rank REAL)''')

# Create a table Links
cur.execute('''CREATE TABLE IF NOT EXISTS Links
    (from_id INTEGER, to_id INTEGER)''')

# Create a table Webs
cur.execute('''CREATE TABLE IF NOT EXISTS Webs (url TEXT UNIQUE)''')

# Check to see if we are already in progress...
# Select a random un-retrieved url from the list
cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
row = cur.fetchone()

# If all the urls are fetched
if row is not None:
    print("Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.")

# If there is no entry in pages table, enter a url to crawl
else :
    starturl = input('Enter web url or enter: ')
    # Default url
    if ( len(starturl) < 1 ) : starturl = 'http://www.dr-chuck.com/'
    if ( starturl.endswith('/') ) : starturl = starturl[:-1]
    web = starturl
    if ( starturl.endswith('.htm') or starturl.endswith('.html') ) :
        pos = starturl.rfind('/')
        web = starturl[:pos]

    # If there is a url in web variable, insert it into pages and webs table
    if ( len(web) > 1 ) :
        cur.execute('INSERT OR IGNORE INTO Webs (url) VALUES ( ? )', ( web, ) )
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) )
        conn.commit()

# Get the current webs
# This code snippet is to extract the current website we are going to crawl
cur.execute('''SELECT url FROM Webs''')
webs = list()
for row in cur:
    webs.append(str(row[0]))

# Print the current url we are going to crawl
print(webs)

many = 0
while True:
    if ( many < 1 ) :
        # Ask how many pages to crawl from the pages table
        sval = input('How many pages:')
        # Break the loop if no input is given
        if ( len(sval) < 1 ) : break
        many = int(sval)
    many = many - 1

    # Select a random un-retrieved url from the list
    cur.execute('SELECT id,url FROM Pages WHERE html is NULL and error is NULL ORDER BY RANDOM() LIMIT 1')
    try:
        row = cur.fetchone()
        # print row
        fromid = row[0]
        url = row[1]
    except:
        # If all the urls are fetched
        print('No unretrieved HTML pages found')
        many = 0
        break

    # Print the url with its id
    print(fromid, url, end=' ')

    # If we are retrieving this page, there should be no links from it
    cur.execute('DELETE from Links WHERE from_id=?', (fromid, ) )
    try:
        # Request information from the url and store it in document
        document = urlopen(url, context=ctx)

        # Store the string version of the retrieved data in html
        html = document.read()

        # If we do not get 200 as our code then page has error
        if document.getcode() != 200 :
            print("Error on page: ",document.getcode())
            # Update error cell of the table for that url in pages table
            cur.execute('UPDATE Pages SET error=? WHERE url=?', (document.getcode(), url) )

        # If the website is a non HTML or no text page, ignore the search and delete the url from pages table
        if 'text/html' != document.info().get_content_type() :
            print("Ignore non text/html page")
            # Deleting the url row from pages table
            cur.execute('DELETE FROM Pages WHERE url=?', ( url, ) )
            conn.commit()
            continue

        # Print the length of the retrieved data
        print('('+str(len(html))+')', end=' ')

        # Parse HTML using BeautifulSoup to get more readable view of HTML
        soup = BeautifulSoup(html, "html.parser")

    # If uer interrupts the program, quit
    except KeyboardInterrupt:
        print('')
        print('Program interrupted by user...')
        break

    # If not able to retrieve data, quit
    except:
        print("Unable to retrieve or parse page")
        # Set error cell information of url on pages table as -1
        cur.execute('UPDATE Pages SET error=-1 WHERE url=?', (url, ) )
        conn.commit()
        continue

    # Update the pages table with new urls fetched from the crawl
    cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( url, ) )

    # Update the url information of the current crawled url
    cur.execute('UPDATE Pages SET html=? WHERE url=?', (memoryview(html), url ) )
    conn.commit()

    # Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        # Get url from the retrieved data
        href = tag.get('href', None)
        # if there is no url, go to the next item
        if ( href is None ) : continue
        # Resolve relative references like href="/contact"
        up = urlparse(href)
        if ( len(up.scheme) < 1 ) :
            href = urljoin(url, href)
        # If # is founf in url, extract url only until #
        ipos = href.find('#')
        if ( ipos > 1 ) : href = href[:ipos]
        # If url is an image or gif, skip that url
        if ( href.endswith('.png') or href.endswith('.jpg') or href.endswith('.gif') ) : continue
        if ( href.endswith('/') ) : href = href[:-1]
        # print href
        if ( len(href) < 1 ) : continue

		# Check if the URL is in any of the webs
        found = False
        for web in webs:
            if ( href.startswith(web) ) :
                found = True
                break
        if not found : continue


        # Update the pages table with new urls fetched from the crawl
        cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( href, ) )
        count = count + 1
        conn.commit()

        cur.execute('SELECT id FROM Pages WHERE url=? LIMIT 1', ( href, ))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:
            print('Could not retrieve id')
            continue
        # print fromid, toid
        cur.execute('INSERT OR IGNORE INTO Links (from_id, to_id) VALUES ( ?, ? )', ( fromid, toid ) )


    print(count)

cur.close()
