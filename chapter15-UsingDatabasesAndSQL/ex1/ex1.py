# Python program - Counting email in database

# Import sqlite library
import sqlite3

# Give a database name to connect to it
# if there is no database with this name, it will create onw
conn = sqlite3.connect('emaildb.sqlite')
# Make a cursor to connect to the database
cur = conn.cursor()

# SQL command to drop the table counts if it exists
cur.execute('''
drop table if exists counts
''')

# SQL command to create table with name counts
cur.execute('''
create table counts (email text, count integer)
''')

# Choose a file to extract and count the email re-occurances
fname = input("Enter file name: ")
if len(fname) < 1: fname = 'mbox-short.txt' # Default file

fh = open(fname)
for line in fh:
    # Select only lines that have email in it
    if not line.startswith("From: "): continue
    pieces = line.split()
    email = pieces[1]
    # SQL command to check if email is present in the database
    cur.execute("select count from counts where email = ?", (email,))
    # Select first row from the query
    row = cur.fetchone()
    # If there are no rows with that email, create one with count = 1
    if row is None:
        cur.execute("insert into counts (email, count) values (?,1)", (email,))
    # Else increment the count value
    else:
        cur.execute("update counts set count = count + 1 where email = ?", (email,))
    # Finally make changes to the memory
    conn.commit()

# SQL command to extract the data and set it in descending order
sqlstr = "select email, count from counts order by count desc limit 10"

# Extract data from table and print it
for row in cur.execute(sqlstr):
    print(row[0],":",row[1])

# Close the connection to database
cur.close()
