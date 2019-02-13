#Import MySQL Connector for DB Activities#
import mysql.connector as mysql

# DB connection Parameters #

def __connect():
    mydb = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "test"
    )
    if mydb:
        return mydb
    else:
        exit("DB is not connnected")