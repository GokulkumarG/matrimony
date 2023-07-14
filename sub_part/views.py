from django.shortcuts import render,redirect
from django.http import HttpResponse
from sub_part.models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
import datetime
from django.urls import path
import os

# Create your views here.\
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def register_form_submission(request):
    if request.method == 'POST':
        if register_data.objects.filter(email_id=request.POST.get('email_id'),phone_number=request.POST.get('phone_number')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this emaild & phonenumber has already registered',extra_tags='already')
            return render(request,'register.html')
        elif register_data.objects.filter(email_id=request.POST.get('email_id')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this emaild has already registered',extra_tags='already')
            return render(request,'register.html')
        elif register_data.objects.filter(phone_number=request.POST.get('phone_number')):
            print("*****already registered****")
            #error message show in frontend
            messages.error(request,'this phone_number has already registered',extra_tags='already')
            return render(request,'register.html')
        else:
            ex1=register_data(first_name=request.POST.get('first_name'),
                          last_name=request.POST.get('last_name'),
                          email_id=request.POST.get('email_id'),
                          phone_number=request.POST.get('phone_number'),
                          gender=request.POST.get('gender'),
                          salary=request.POST.get('salary'),
                          study=request.POST.get('qualification'),
                          designation=request.POST.get('designation'),
                          file=request.FILES['file'],
                          password=request.POST.get('password'),
                          date_birth=request.POST.get('date_birth'))
            ex1.save()
            email=request.POST.get('email_id')
            password=request.POST.get('password')
            phone_number=request.POST.get('phone_number')
            ex2=login_data(email_id=email,password=password,phone_number=phone_number)
            ex2.save()
            print("Registered Successfully")
            #mail send code****************
            first_name=request.POST.get('first_name')    
            last_name=request.POST.get('last_name')
            email_id=request.POST.get('email_id')
            gender=request.POST.get('gender')
            phone_number=request.POST.get('phone_number')
            salary=request.POST.get('salary')
            designation=request.POST.get('designation')
            password=request.POST.get('password')
            date_birth=request.POST.get('date_birth')
            
            subject = 'TamilMatrimony'
            message = f'Hi thank you for registering in TamilMatrimony \n First Name={first_name} \n Last Name={last_name}\n Email_id={email_id}\n Gender={gender}\n Date-Of-Birth={date_birth}\n Phone Number={phone_number}\n Salary={salary}\n Designation={designation}\n Password={password}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail( subject, message, email_from, recipient_list )
            print("****mail send successfully***")
            #*******************************************************
            msg="Registered Successfully"
            messages.success(request,"Registered Successfull")
            return render(request,'login.html',{'msg':msg})
    else:
        print("****data failed****")
        return render(request,'register.html')
        
    

def login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')
def admin(request):
    return render(request,'admin.html')

def admin2(request):
    return render(request,'admin2.html')

def add_admin(request):
    return render(request,'add_admin.html')

def admin_login(request):
    if request.method == "POST":
        if admin_data.objects.filter(user_name=request.POST.get('user_name'),password=request.POST.get('password')):
            name=admin_data.objects.get(user_name=request.POST.get('user_name'),password=request.POST.get('password'))
            print("**admin login successfully**")
            msg="admin login successfully"
            output=register_data.objects.all().count()
            registered=register_data.objects.all()
            login_time=datetime.datetime.now()
            deleted=deleted=register_data.objects.filter(status="married").count()
            
            return render(request,'admin2.html',{'deleted':deleted,'msg':msg,'output':output,'registered':registered,'name':name,'login_time':login_time})
        
        else:
            messages.error(request,'please cheack your username or password',extra_tags='failed')
            return render(request,'admin.html')

def login_submission(request):
    if request.method  == "POST":
        if register_data.objects.filter(Q(email_id=request.POST.get('email_id'))| Q(phone_number=request.POST.get('email_id')),password=request.POST.get('password')):
            print("***login successfully****")
            logger_data=register_data.objects.get(Q(email_id=request.POST.get('email_id'))| Q(phone_number=request.POST.get('email_id')))
              
            if logger_data.gender == "male":
                data=register_data.objects.filter(gender="female")
                count=data.count()
                main=data
                msg="Female"
    
                return render(request,'dashboard.html',{'msg':msg,'logger_data':logger_data,'output':data,'count':count,'main':main})
            if logger_data.gender == "female":
                data=register_data.objects.filter(gender="male")
                count=data.count()
                main=data
                msg="Male"
            
                return render(request,'dashboard.html',{'msg':msg,'logger_data':logger_data,'output':data,'count':count,'main':main})
    
            
        else:
            print("***failed login****")
            messages.error(request,'check your email_id  or password',extra_tags='failed')
            return render(request,'login.html')
    else:
        return HttpResponse('<h1 style="color:red;text-align:center    " >Only Logging Data </h1>')
    
    
def back(request,id):
    rem=register_data.objects.get(id=id)
    if rem.gender == "male":
        data=register_data.objects.filter(gender="female")
        count=data.count()
        main=data
        msg="Female"
        return render(request,'dashboard.html',{'msg':msg,'logger_data':rem,'output':data,'count':count,'main':main})
    if rem.gender == "female":
        data=register_data.objects.filter(gender="male")
        count=data.count()
        main=data
        msg="Male"
    
        return render(request,'dashboard.html',{'msg':msg,'logger_data':rem,'output':data,'count':count,'main':main})
       
def profile(request,id):
    get1=register_data.objects.get(id=id) 
      
    if request.method == "POST":
        
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email_id=request.POST.get('email_id')
        phone_number=request.POST.get('phone_number')
        gender=request.POST.get('gender')
        salary=request.POST.get('salary')
        study=request.POST.get('qualification')
        designation=request.POST.get('designation')
        file=request.FILES['file']
        password=request.POST.get('password')
        date_birth=request.POST.get('date_birth')
        status=request.POST.get('status')
            
        get1.first_name=first_name
        get1.last_name=last_name
        get1.email_id=email_id
        get1.phone_number=phone_number
        get1.gender=gender
        get1.salary=salary
        get1.study=study
        get1.designation=designation
        get1.file=file   
        get1.password=password
        get1.date_birth=date_birth
        get1.status=status
               
        get1.save()
            
        messages.error(request,'Data Saved Successfully',extra_tags='saved')
        return render(request,'profile.html',{'get1':get1})
           
       
    return render(request,'profile.html',{'get1':get1})


   
def delete_id(request,id):
    ex1=register_data.objects.get(id=id)
    first_name=ex1.first_name
    last_name=ex1.last_name
    email_id=ex1.email_id
    phone_number=ex1.phone_number
    gender=ex1.gender
    date_birth=ex1.date_birth
    salary=ex1.salary
    study=ex1.study
    designation=ex1.designation
    file=ex1.file
    password=ex1.password
    status=ex1.status
    var=deleted_data(first_name=first_name,last_name=last_name,email_id=email_id,phone_number=phone_number,gender=gender,date_birth=date_birth,salary=salary,study=study,designation=designation,file=file,password=password,status=status)
    var.save()
    ex1.delete()
    os.remove(ex1.file.path)
    output=register_data.objects.all().count()
    registered=register_data.objects.all()
    login_time=datetime.datetime.now()
    deleted=deleted_data.objects.all().count()
            
    return render(request,'admin2.html',{'deleted':deleted,'output':output,'registered':registered,'login_time':login_time})

def status_filter(request):
    if register_data.objects.filter(status=request.POST.get('status_data')):
        registered=register_data.objects.filter(status=request.POST.get('status_data'))
        
        output=register_data.objects.all().count()
        login_time=datetime.datetime.now()
        deleted=register_data.objects.filter(status="married").count()
        return render(request,'admin2.html',{'deleted':deleted,'output':output,'registered':registered,'login_time':login_time})
    else:
        messages.error(request,'No Such Data Please Type "married" Only',extra_tags='failed')
        output=register_data.objects.all().count()
        login_time=datetime.datetime.now()
        deleted=deleted_data.objects.all().count()
        return render(request,'admin2.html',{'deleted':deleted,'output':output,'login_time':login_time})
    
def add_admin_data(request):
    if request.method == 'POST':
        if admin_data.objects.filter(user_name=request.POST.get('user_name'),password=request.POST.get('password')):
            print("*****already have account****")
            #error message show in frontend
            messages.error(request,'this username & password has already saved',extra_tags='already')
            return render(request,'add_admin.html')
        else:
            ex1=admin_data(user_name=request.POST.get('user_name'),
                       password=request.POST.get('password'))
            ex1.save()
            return render(request,'admin.html')