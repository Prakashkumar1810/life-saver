from django.shortcuts import render

# Create your views here.

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
	c = {}
	if request.method == 'POST':
		c['email'] = request.POST.get('email')
		c['password'] = request.POST.get('password')
	
	return render(request,'life/dashboard.html',c)
		