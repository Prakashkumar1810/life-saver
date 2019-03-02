import pymysql

connection = pymysql.connect("localhost","root","helloworld","lifesaver")
cursor = connection.cursor()

#name = input("Enter name : ")

query = "SELECT * FROM donors;"

try:
	cursor.execute(query)
	#connection.commit()
	data = cursor.fetchall()
	for i in data:
		print(i[0])
	#print(data)
	
except Exception as e:
	#connection.rollback()
	print(e)

connection.close()