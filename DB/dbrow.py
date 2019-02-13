import dbcon

mycursor = dbcon.mydb.cursor()

mycursor.execute("select * from customer ")

#customData = mycursor.fetchall()

for val in mycursor:
    print(val)
    """print("Customer ID :", val[0])
    print("Customer Name :",val[1])
    print("Customer Age : ",val[2])"""
