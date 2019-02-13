import dbcon

conn = dbcon.__connect()

cursor = conn.cursor()

cursor.execute("Select * from customer where age < 40")

customerData = cursor.fetchall()

for data in customerData:
    print(data)
"""
data = cursor.fetchone()
assert isinstance(data, object)
print(data)
"""