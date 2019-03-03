from django.shortcuts import render
from django.http import HttpResponse
from .dbms import account
# Create your views here.
global data
data = {}

def life(request):
	return render(request,'life/life.html')

def about(request):
	return render(request,'life/about.html')

def contact(request):
	return render(request,'life/contact.html')

def login(request):
	return render(request,'life/login.html')

def search(request):
	return render(request,'life/search.html')

def sign(request):
	return render(request,'life/sign.html')

def get_in(request):
	#data = {}
	if request.method == 'POST':
		data['phone'] = request.POST.get('phone')
		data['password'] = request.POST.get('password')
	
	if account.log_in(data):
		return render(request,'life/after.html',data)
	else:
		return HttpResponse("<h1>Log in failed</h1><p>Check username and password</p>")

def create_acc(request):
	data = {}
	if request.method == 'POST':
		data['name'] = request.POST.get('name')
		data['city'] = request.POST.get('city')
		data['email'] = request.POST.get('email')
		data['phone'] = request.POST.get('mobile')
		data['bloodgroup'] = request.POST.get('group1')
		data['password'] = request.POST.get('password')
	
	if account.create(data):
		return render(request,'life/dashboard.html',data)
	else:
		return HttpResponse("<h1>signup failed</h1>")

def update_date(request):
	if request.method == 'POST':
		data['day'] = request.POST.get('day')
	
	if account.update_date(data):
		return HttpResponse('<h1>Date updated successfully</h1><p><a href="login"><button type="button">Go back</button></a></p>')
	else:
		return HttpResponse('<h1>Update failed</h1><p><a href="login"><button type="button">Go back</button></a></p>')

def delete(request):
	if account.delete(data):
		return HttpResponse('<h1>Account deleted successfully</h1><p><a href="life"><button type="button">Home</button></a></p>')
	else:
		return HttpResponse('<h1>Deletion failed</h1><p><a href="life"><button type="button">Home</button></a></p>')
