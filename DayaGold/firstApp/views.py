from django.shortcuts import render
from .models import User

# Create your views here.

def jewellery(request):
	user_name = request.POST.get('username')
	pass_word = request.POST.get('password')
	try:
		current_user = User.objects.get(username = user_name)
	except:
		return render(request, 'registration/login.html',{})
		
	if pass_word == current_user.password:
		return render(request, 'firstApp/firstPage.html',{})
	
	return render(request, 'registration/login.html',{})


def register(request):
	user_name = request.POST.get('username')
	email_add = request.POST.get('email')
	psw = request.POST.get('psw')
	add = request.POST.get('address')
	ag_e = request.POST.get('age')
	mob = request.POST.get('mobile')
	current_user = User(username = user_name, password = psw, mobile=mob, address = add,email = email_add,age =ag_e)
	current_user.save()
	
	return render(request, 'registration/login.html',{})
