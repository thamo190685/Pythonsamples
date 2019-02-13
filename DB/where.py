import dbcon

mydb = dbcon.__connect()

cursor = mydb.cursor()

sql = 'select * from customer where age = 34'

val = '34'

cursor.execute(sql)

customerData = cursor.fetchall()

for data in customerData:
    print(data)
