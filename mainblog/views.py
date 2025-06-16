from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from . import forms
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form':form}
    
    return render(request, 'blog/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('posts')
    
    else:
        form = AuthenticationForm()
    
    context = {'form':form}
    return render(request, 'blog/login.html', context)



def logout_user(request):
    logout(request)
    return redirect('login')





#BLOG VIEWS!!!!!

def posts(request):
    blogs = Blog.objects.all().order_by('-date_uploaded')
    
    context = {
        'blogs':blogs
    }
    return render(request,'blog/posts.html', context)

def post_detail(request, id):
    blog = Blog.objects.get(id=id)

    context = {
        'blog':blog
    }
    return render(request, 'blog/post_detail.html', context )


def add_post(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to add a post.')
        return redirect('login')

    if request.method == 'POST':
        form = BlogForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts')


    else:
        form = BlogForm()
 
    context = {'form':form}
    return render(request, 'blog/add_post.html', context)


def update_post(request, id):
    #blog = Blog.objects.get(id=id)
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user:
        messages.error(request, 'You are not authorized to make changes')
        return redirect('login')
    
    if request.method == 'POST':
        form = BlogForm(request.POST or None, instance=blog)

        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('posts')
    
    else:
        form = BlogForm(instance=blog)
    
    context = {
        'blog':blog,
        'form':form
    }
    return render(request,'blog/update_post.html', context)


def delete_post(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author == request.user:
        blog.delete()
        messages.success(request, 'Post delete successful.')
    else:
        messages.error(request, 'You are not authorized to delete this post.')
    
    return redirect('posts')
    
   
