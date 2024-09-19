from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import EmailMessage
# Create your views here.

@login_required(login_url='login_page')
def index(request):
   
    return render(request, 'layout/index.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')
    return render(request, 'pages/pages-login.html')

def logoutPage(request):
    logout(request)
    return redirect('login_page')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index_page')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_page')
        context = {
                'form':form
            }
        return render(request, 'pages/pages-register.html', context)

def profile(request):
    return render(request, 'pages/users-profile.html')

def contactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success_page')
    return render(request, 'pages/contact.html')

def success(request):
    return HttpResponse('Success!')