from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog
from django.utils import timezone

# Client Side Views
def aboutUS(request):
    return render(request, 'aboutus.html')

def addBlogUser(request):
    return render(request,'add-blog.html')

def blog(request):
    return render(request, 'blog.html')

def home(request):
    return render(request, 'home.html')

def landingPage(request):
    return render(request, 'pages/index.html')

def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')

# Admin Side Views
def addBlogAdmin(request):
    return render(request, 'Addblog.html')

def updateBlogAdmin(request):
    return render(request, 'updateblog.html')

def blogListAdmin(request):
    return render(request, 'bloglist.html')


def home(request):
    recent_blogs = Blog.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
    featured_blogs = Blog.objects.filter(featured=True, created_at__lte=timezone.now()).order_by('-created_at')[:4]

    return render(request, 'home.html', {
        'recent_blogs': recent_blogs,
        'featured_blogs': featured_blogs,
    })
