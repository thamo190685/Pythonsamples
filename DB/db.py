import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

mycursor = mydb.cursor()


sql = "insert into new (sku) values(%s)"

val = [("new1001"),("new234234243"),("new12312")]

print(sql, val)

mycursor.executemany(sql,val) 

mydb.commit()

print(mycursor.rowcount, ' was inserted')
