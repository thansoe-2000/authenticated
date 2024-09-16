from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login_page')
def index(request):
    return render(request, 'layout/index.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')
    return render(request, 'pages/pages-login.html')

def register(request):
    return render(request, 'pages/pages-register.html')

def profile(request):
    return render(request, 'pages/users-profile.html')