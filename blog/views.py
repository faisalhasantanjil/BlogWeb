from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')

    return render(request, 'blog/login.html')


@login_required(login_url='signin')
def home(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        user = UserInformation.objects.get(user=request.user.id)
        if form.is_valid():
            form.instance.author = user
            form.save()
            return redirect('home')
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'form': form,
    }
    return render(request, 'blog/home.html', context)


def detailedblog(request, pk_test):
    blog = Blog.objects.get(id=pk_test)
    form = CommmentForm()
    comments = Comment.objects.filter(blog=pk_test)
    print(blog)
    if request.method == 'POST':
        form = CommmentForm(request.POST)
        form.instance.author = UserInformation.objects.get(
            user=request.user.id)
        form.instance.blog = blog
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(request.path_info)
            # return redirect('detailedblog')
    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/detailedblog.html', context)


def Commentbox(request, pk_test):
    blog = Blog.objects.get(id=pk_test)
    print(blog)
    context = {
        'blog': blog,
    }
    return render(request, 'blog/detailedblog.html', context)
