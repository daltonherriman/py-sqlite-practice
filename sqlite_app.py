# Imports
import sqlite3 

# Create connection object that represents the database
#   -Can pass in a file name for the database or use an in-memory DB
#   -conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('cars.db')

# Verify "conn" object was created successfully
print(conn.total_changes) # Total number of DB rows changed by "conn"

# Returns a cursor object that allows us to send SQL statements to the DB w/ "cursor.execute()"
cursor = connection.cursor()

# Create table "cars" with 3 columns; one for 'make', 'model' and 'miles'
cursor.execute("CREATE TABLE cars (make TEXT, model TEXT, miles INTEGER)")

# Insert two rows of data into table: 'cars'
cursor.execute("INSERT INTO cars VALUES ('Jeep', 'Wrangler', 90000)")
cursor.execute("INSERT INTO cars VALUES ('Chevy', 'Silverado', 120000)")