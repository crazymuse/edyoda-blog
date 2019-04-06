from django.http import HttpResponse
from .models import Blog, User,Status
from django.shortcuts import render
from base64 import b64encode, b64decode
from django.core.urlresolvers import reverse
from django.utils import timezone

import hashlib, binascii, os



def index(request):
    """
    This view will contain the blog lists
    """
    blogs_list = Blog.objects.order_by('-first_published')[:5]
    context = {'blogs_list':blogs_list,'username':get_username(),'status':get_status()}
    print (blogs_list)
    return render(request,'blogs/index.html',context)

def login(request):
    return render(request, 'blogs/login.html',{'status':get_status(),'username':get_username()})

def logout(request):
    logout_action()
    return render(request, 'blogs/login.html',{'status':get_status(),'username':get_username()})


def write(request):
    return render(request, 'blogs/write.html',{'status':get_status(),'username':get_username()})

def profile(request):
    return render(request, 'blogs/profile.html',{'status':get_status(),'username':get_username()})

 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

def login_check(func):
    def inner1(request):
        print (len(User.objects.filter(username=request.POST['username'])))
        if len(User.objects.filter(username=request.POST['username']))<1:
            return render(request, 'blogs/login.html',{'message':'No such user','page':'LOGIN','status':get_status(request.POST['username'])})

        for user in User.objects.filter(username=request.POST["username"]):
            if user.status == "LOGIN":
                return render(request, 'blogs/login.html',{'message':'Already Logged in','page':'LOGIN','username':get_username(),'status':get_status(request.POST['username'])})
            if (len(User.objects.filter(status='LOGIN'))>=1):
                return render(request, 'blogs/login.html',{'message':'Already Logged in','page':'LOGIN','username':get_username(),'status':get_status(request.POST['username'])})
            print (user.username,user.password,request.POST["password"])
            if verify_password(stored_password=user.password,provided_password=request.POST["password"]):
                print ("same password")
                return func(request) 
            
        return  render(request, 'blogs/login.html',{'message':'Enter the correct password','page':'LOGIN'})
    return inner1

def register_check(func):
    def inner1(request):
        if len(User.objects.filter(username=request.POST['usernamesignup']))>=1:
            return render(request, 'blogs/login.html',{'message':'Already Created','page':'SIGNUP','username':get_username(),'status':get_status(request.POST['usernamesignup'])})
        else:
            return func(request)
            
    return inner1;


def write_check(func):
    def inner1(request):
        if len(request.POST['title'])<5:
            return render(request, 'blogs/write.html',{'message':'title too small','username':get_username(),'status':get_status()})
        if len(request.POST['detail'])<5:
            return render(request, 'blogs/write.html',{'message':'detail too small','username':get_username(),'status':get_status()})
        if get_status() != "LOGIN":
            return render(request, 'blogs/write.html',{'message':'user not logged in','username':get_username(),'status':get_status()})
        return func(request)
    return inner1
           
 

def register_action(username,password):
    u = User(username=username,password=hash_password(password),created_on=timezone.now(),last_logged_in=timezone.now(),status="LOGIN")
    u.save()

def write_action(title,detail,username):
    for u in User.objects.filter(username=username):
        b = Blog(title=title,body=detail,status="PUBLISHED",first_published= timezone.now(),last_edited = timezone.now(),user=u)
        b.save()

def login_action(username,password):
    for user in User.objects.filter(username=username):
        user.status = 'LOGIN'
        user.last_logged_in = timezone.now()
        user.save();


def logout_action():
    for user in User.objects.filter(status='LOGIN'):
        user.status = 'LOGOUT'
        user.save();





def get_username():
    username="DEFAULT"
    for user in User.objects.filter(status="LOGIN"):
        username = user.username
    print ('USERNAME : ',username)
    return username


def get_status(username='DEFAULT'):
    for user in User.objects.filter(status="LOGIN"):
        username = user.username

    if len(User.objects.filter(username=username))==0:
        print ('LOGOUT')
        return 'LOGOUT'
    for user in User.objects.filter(username=username):
        print (user.status)
        return user.status

@register_check
def userregister(request):
    print ('Registering here');
    username = request.POST['usernamesignup']
    password = request.POST['passwordsignup']
    print (username,password)
    register_action(username,password)
    return render(request, 'blogs/index.html',{'username':get_username(),'status':get_status(request.POST['usernamesignup'])})

@login_check
def userlogin(request):
    print ('Login here');
    print (request.POST)
    username = request.POST['username']
    password = request.POST['password']
    login_action(username,password)
    return render(request, 'blogs/index.html',{'username':get_username(),'status':get_status(request.POST['username'])})


@write_check
def userwrite(request):
    title  = request.POST["title"]
    detail  = request.POST["detail"]
    write_action(title,detail,get_username())
    return render(request, 'blogs/index.html',{'username':get_username(),'status':get_status()})


if __name__=="__main__":
    pass

