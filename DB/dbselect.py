import mysql.connector as mysql

try:
 mydb =  mysql.connect(host="localhost",user="root",passwd="",database="test")
 print(mydb)
 if mydb:
  mycur = mydb.cursor()
  mycur.execute("SELECT * FROM new")
  rowval = mycur.fetchall()
  for val in rowval:
   print(val)
 else:
  print('DB failure')
except:
 print('No DB selected')	