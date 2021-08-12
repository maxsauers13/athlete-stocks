import mysql.connector

# creates a connection to the mysql database
def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Lville2019",
        database="nba-trading-schema"
    )

    return mydb