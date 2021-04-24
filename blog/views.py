from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django_blog.settings import EMAIL_HOST_USER
from django.conf import settings
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'blog/home.html')

def create(request):
    form = BlogForm()
    if request.method=='POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

    context= {'form' : form}
    return render(request,'blog/create.html',context)
     

def displayBlog(request):
    blog = BlogModel.objects.all()
    context = {'blog':blog}
    return render(request,'blog/display.html',context)       


def deletelist(request, id): 
    # fetch the object related to passed id 
    blog = get_object_or_404(BlogModel, id = id) 
    if request.method =="POST": 
        # delete object 
        blog.delete() 
        # after deleting redirect to home page 
        return redirect("/") 
    context = {}
    return render(request, "blog/delete.html", context) 

def updatelist(request, id): 
    blog = get_object_or_404(BlogModel, id = id)  
    form = BlogForm(instance = blog)
    if(request.method == 'POST'):
        form = BlogForm(request.POST, instance = blog)
        if form.is_valid():
            form.save()
        return redirect('/')
    context ={'form':form}
    return render(request,'blog/update.html',context)

def sendmail(request,id):
    sub = Subscribe()
    blog = BlogModel.objects.get(id=id)
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject = str(sub['sub'].value())    # 'Sending emails thorugh Django'
        message = "Title - " + str(blog.title) + " .Description - " + str(blog.description)   
        recepient = str(sub['Email'].value())  # through forms.py Email field
        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'blog/success.html', {'recepient': recepient})
    return render(request, 'blog/sendblogmail.html', {'form':sub})


