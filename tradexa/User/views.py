
from django.shortcuts import render
from.forms import Login,PostForm
from .models import User,Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages


# Create your views here.
def showformdata1(request):
    if request.method == 'POST':
        fm=Login(request.POST)
        if fm.is_valid():
            
            fn = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            nm = fm.cleaned_data['username']
            #  print(fn)
            #  print(ln)
            #  print(em)
            #  print(pw)
            #  print(nm)
            regi = User(first_name=fn, last_name=ln, email=em, password=pw, username=nm)
            regi.save()
            
    else:
        fm=Login() 
    return render(request,'User/login.html',{'form':fm})




# Create your views here.
# @login_required
def showformdata2(request):
    if request.method == 'POST':
        fm=PostForm(request.POST)
        if fm.is_valid():
            
            us = fm.cleaned_data['user']
            tx = fm.cleaned_data['text']
            cr = fm.cleaned_data['created_at']
            ur = fm.cleaned_data['updated_at']
            #  print(us)
            #  print(tx)
            #  print(cr)
            #  print(ur)
            regis = Post(user=us, text=tx, created_at=cr, updated_at=ur)
            regis.save()
            
    else:
        fm=PostForm() 
    return render(request,'User/postform.html',{'form':fm})



