from flask import Flask
import mysql.connector as mySQLConnector #import mySQL-Python connector

# Main package to connect to files
def db_connect():
    # Create connection with active mySQL server
    conn = mySQLConnector.connect(host="localhost", user="root", passwd="milomilo")
    q_db = conn.info_query("SHOW DATABASES")


    if conn:
        print("Connection successful.")
    else:
        print("Could not connect.")

    # Create a curser object to traverse the db
    cur = conn.cursor()
    cur.execute("SHOW DATABASES")
    for row in cur:
        print(row)

db_connect()