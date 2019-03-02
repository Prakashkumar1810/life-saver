#imports
import pymysql
#functions

def create(data):
	connection = pymysql.connect("localhost","root","helloworld","lifesaver")
	cursor = connection.cursor()
	
	query = "INSERT INTO donors VALUES('{}','{}','{}','{}','{}','{}','1998-07-08');".format(data['name'],data['city'],data['email'],data['phone'],data['bloodgroup'],data['password'])
	
	try:
		cursor.execute(query)
		connection.commit()
		flag = True
	except Exception as e:
		connection.rollback()
		print(e)
		flag = False
	
	connection.close()
	return flag