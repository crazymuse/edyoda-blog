from django.http import HttpResponse
from .models import Blog
from django.shortcuts import render

def index(request):
    """
    This view will contain the blog lists
    """
    blogs_list = Blog.objects.order_by('-first_published')[:5]
    context = {'blogs_list':blogs_list}
    print (blogs_list)
    return render(request,'blogs/index.html',context)

def login(request):
    return render(request, 'blogs/login.html',{})

def write(request):
    return render(request, 'blogs/write.html',{})

def profile(request):
    return render(request, 'blogs/profile.html',{})

def userregister(request):
    print ('Registering here');
    print (request.POST)
    return render(request, 'blogs/login.html',{})


def userlogin(request):
    print ('Login here');
    print (request.POST)
    return render(request, 'blogs/login.html',{})



