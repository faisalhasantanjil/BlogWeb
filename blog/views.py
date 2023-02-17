from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.


def register(request):
    form = UserForm()
    print(form)
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        form.instance.username = request.POST['email']
        if form.is_valid():
            login(request, form.save())
            UserInformation.objects.create(user=request.user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'blog/register.html', context)


def signin(request):
    return render(request, 'blog/login.html')


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/home.html', context)


def detailedblog(request, pk_test):
    blog = Blog.objects.get(id=pk_test)
    comments = Comment.objects.filter(blog=pk_test)
    print(blog)
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blog/detailedblog.html', context)


def Commentbox(request, pk_test):
    blog = Blog.objects.get(id=pk_test)
    print(blog)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/detailedblog.html', context)
