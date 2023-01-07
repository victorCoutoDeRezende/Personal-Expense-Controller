#importing SQLite
import sqlite3 as lite

#Creating connection
con = lite.connect('data.db') #con = connection

#Creating category tables
with con:
    cur = con.cursor() #cur = cursor
    cur.execute("CREATE TABLE Category(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

#Creating income tables
with con:
    cur = con.cursor() #cur = cursor
    cur.execute("CREATE TABLE Income(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, added_in DATE, value DECIMAL)")

#Creating spending tables
with con:
    cur = con.cursor() #cur = cursor
    cur.execute("CREATE TABLE Spending(id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, spent_in DATE, value DECIMAL)")