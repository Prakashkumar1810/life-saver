#imports
from django.shortcuts import render
from django.http import HttpResponse
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

def log_in(data):
	connection = pymysql.connect("localhost","root","helloworld","lifesaver")
	cursor = connection.cursor()
	
	query = "SELECT phone,name,password from donors where phone='{}'".format(data['phone'])
	
	try:
		cursor.execute(query)
		values = cursor.fetchone()
		if values[2]==data['password']:
			data['name'] = values[1]
			flag = True
		else:
			flag = False
	except Exception as e:
		flag = False
		print(e)
	
	connection.close()
	return flag