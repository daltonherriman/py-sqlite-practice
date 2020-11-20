# Imports
import sqlite3 

# Create connection object that represents the database
#   -Can pass in a file name for the database or use an in-memory DB
#   -conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('employee.db')