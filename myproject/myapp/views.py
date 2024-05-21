from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from datetime import datetime
from myapp.models import Contact
from myapp.models import Appointment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from myapp.models import Bookings
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def appointment(request):

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        department = request.POST.get('department')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time')
        bmi= request.POST.get('bmi')
        doctor= request.POST.get('doctor')
        slot= request.POST.get('slot')
        summary= request.POST.get('summary')
        day= request.POST.get('day')
        report= request.FILES.get('report')
        
        if Bookings.objects.filter(doctor=doctor,slot=slot,day=day).exists():   
            return render(request,"appointment.html",{'prompt':'This slot is booked!'})

        Bookings.objects.create(doctor=doctor,slot=slot,day=day,patient_name=name)
        # appointment=Appointment(name=name, age=age, phone=phone, email=email, department=department, address=address, date=date, time=time,bmi=bmi,doctor=doctor,slot=slot,day=day,summary=summary,report=report)
        # appointment.save()
        Appointment.objects.create(name=name, age=age, phone=phone, email=email, department=department, address=address, date=date, time=time,bmi=bmi,doctor=doctor,slot=slot,day=day,summary=summary,report=report)

        messages.success(request, "Your message has been sent")
    else:
        name = ''
        age=''
        phone=''
        email=''
        department=''
        address=''
        date=''
        time=''


    return render(request, "appointment.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact=Contact(name=name, email=email, subject=subject, phone=phone, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
    else:
        name = ''
        email = ''
        subject = ''
        phone = ''
        message = ''
    
        
    return render(request, "contact.html")

def doctor(request):
    return render(request, "doctor.html")

def gallery(request):
    return render(request, "gallery.html")

def login(request):
    return render(request, "login.html")

def privacy(request):
    return render(request, "privacy.html")

def registration(request):
    return render(request, "registration.html")

def terms(request):
    return render(request, "terms.html")

def bmi(request):
    return render(request, "bmi.html")


def handelSignup(request):
    if request.method == 'POST' :
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password= request.POST['password']
        confirm= request.POST['confirm']

        # check for errorneous inputs
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already exists")
            return redirect('/')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already exists")
            return redirect('/')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username should only contain letter and numbers")
            return redirect('/')
    
        if password != confirm:
            messages.error(request, "password do not match")
            return redirect('/')
    
        


        # create the user
        myuser = User.objects.create_user(username, email, password )
        myuser.first_name = fname
        myuser.last_name = lname
        confirm = confirm
        myuser.save()
        messages.success(request, "Your accout has been successfully created")
        return redirect('/')

    else:
        return HttpResponse('404 - Not Found')
    
    
   
def handelLogin(request):
    if request.method == 'POST' :
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword= request.POST['loginpassword']

        user = authenticate(username=loginusername, 
        password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('/')
       
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')
    