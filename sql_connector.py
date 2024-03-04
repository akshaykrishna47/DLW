import mysql.connector

def create_database(database_name):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password"
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE " + database_name)
    return

def create_table(database_name, table_name):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = database_name
    )
    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE "+table_name+"(room_no INT, date_ DATE, time_ INT, booking_status BOOL, PRIMARY KEY (room_no, date_, time_));")
    mycursor.execute("DESCRIBE "+table_name)
    for x in mycursor: print(x)

def insert_data(database_name,table_name):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = database_name
    )
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO Schedule(room_no, date_, time_, booking_status)VALUES('24','2024-03-04', '1200', TRUE)")
    mycursor.execute("SELECT * FROM "+table_name)
    for x in mycursor: print(x)

# create_database("testdata")
# create_table("testdata","Schedule")
insert_data("testdata","Schedule")