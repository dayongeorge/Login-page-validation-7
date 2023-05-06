from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request,'index.html')
@login_required(login_url='login')

def home(request):
    
    return render(request,'home.html')
   # return redirect('index')
    
@never_cache
@login_required(login_url='login')
def loginn(request):
    if 'username' in request.session:
        
        return redirect('home')
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            return redirect('signup')
    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()

        return redirect('login')
    
    return render(request,'signup.html')