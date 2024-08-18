from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Blog
from . import forms
from .forms import BlogForm




# Create your views here.
def home(request):
    template = loader.get_template('blog/home.html')
    return HttpResponse(template.render({}, request))

def posts(request):
    blogs = Blog.objects.all().values()
    template = loader.get_template('blog/posts.html')
    context = {
        'blogs':blogs
    }
    return HttpResponse(template.render(context, request))

def post_detail(request, id):
    blog = Blog.objects.get(id=id)
    template = loader.get_template('blog/post_detail.html')
    context = {
        'blog':blog
    }
    return HttpResponse(template.render(context, request))

def add_post(request):
    submitted = False
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_post?submitted=True')


    else:
        form = BlogForm()
        if 'submitted' in request.GET:
            submitted = True

    template = loader.get_template('blog/add_post.html')
    context = {
        'form':form,
        'submitted':submitted
    }
    return HttpResponse(template.render(context, request))


def update_post(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('posts')
    
    template = loader.get_template('blog/update_post.html')
    context = {
        'blog':blog,
        'form':form
    }
    return HttpResponse(template.render(context, request))

def delete_post(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('posts')