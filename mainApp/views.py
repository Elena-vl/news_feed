from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
	return render(request, 'mainApp/basic.html', {'values':['Если есть вопросы, то не звони', request.POST]})