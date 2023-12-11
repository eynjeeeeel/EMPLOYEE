from django.shortcuts import render
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render (request, 'index.html')

def register(request):
    error =""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['password']
        try:
           user =  User.objects.create_user(first_name=fn, last_name=ln,username=em, password=pwd)
           EmployeeDetail.objects.create(user =user, empcode=ec)
           error="no"
        except:
            error="yes"

    return render (request, 'register.html', locals())

def emp_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username = u, password = p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render (request, 'emp_login.html', locals())

def emp_home(request):
    return render (request, 'emp_home.html')