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
    mycursor.execute("CREATE TABLE "+table_name+"(room_no INT, date_ DATE, time_ INT, booking_status INT, PRIMARY KEY (room_no, date_, time_));")
    mycursor.execute("DESCRIBE "+table_name)
    for x in mycursor: print(x)

def insert_schedule_data(database_name,table_name, room_no,date_,time_,booking_status):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = database_name
    )
    mycursor = db.cursor()
    mycursor.execute("INSERT INTO "+ table_name +" (room_no, date_, time_, booking_status) VALUES(%s,%s,%s,%s)", ( room_no,date_,time_,booking_status))
    db.commit()
    mycursor.execute("SELECT * FROM "+table_name)
    for x in mycursor: print(x)

def get_schedule_data(room_no,date_,time_):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "password",
        database = "testdata"
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT booking_status FROM Schedule WHERE room_no=%s AND date_=%s AND time_=%s",(room_no,date_,time_))
    for x in mycursor: print(x)

# create_database("testdata")
# create_table("testdata","Schedule")
# insert_schedule_data("testdata","Schedule", '29','2024-03-04', '1200', '1')
get_schedule_data('29','2024-03-04', '1200')

