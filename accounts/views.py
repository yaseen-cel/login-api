from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")
def register(request):
    if request.method=='POST':
        print('inside post')
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password == password1:
            if User.objects.filter(username = username).exists():
                print('exist1')
                messages.info(request,'username already exist')
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                print('exist2')
                messages.info(request,'email already exist')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,'Password didnt match')
            print('exist3')
            return redirect('register')
    else:    
        print('exist4')
        return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    if request.method == 'GET':    
        return render(request,"login.html")
def home(request):
    return render(request,'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/')