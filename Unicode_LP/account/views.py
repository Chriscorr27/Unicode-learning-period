from django.shortcuts import render,redirect
from .forms import CreateUser
from .models import myUser
from CRUD_task.models import *
from django.contrib.auth.models import auth
from .decorator import only_superuser,unauthenticated_user,authenticated_user
# Create your views here.
@only_superuser
def create_user(request):
    form = CreateUser()
    is_user=False
    #print(form)
    if(request.method == 'POST'):
        form = CreateUser(request.POST)
        if form.is_valid():
           # print(form)
            user = form.save()
            #user = myUser.objects.get(username=form.cleaned_data['username'])
            App_user.objects.create(user=user)
            return redirect('create_profile',user.id)
        
    content={'form':form,'is_user':is_user}
    return render(request,'register_user.html',content)

@unauthenticated_user
def register_user(request):
    form = CreateUser()
    is_user=True
    #print(form)
    if(request.method == 'POST'):
        form = CreateUser(request.POST)
        if form.is_valid():
           # print(form)
            user = form.save()
            #user = myUser.objects.get(username=form.cleaned_data['username'])
            App_user.objects.create(user=user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            authuser=auth.authenticate(username=username,password=password)
           # print(username,password)
            if authuser is not None :
                auth.login(request,authuser)
                return redirect('create_Myprofile')
        
    content={'form':form,'is_user':is_user}
    return render(request,'register_user.html',content)

@unauthenticated_user
def login_user(request):
    message = ""
    message_style= "invisible"
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        authuser=auth.authenticate(username=username,password=password)
        if authuser is not None :
                auth.login(request,authuser)
                return redirect('home')
        else:
            try:
                user = myUser.objects.get(username=username)
                message = "Username and password doesnot match"
                message_style = "visible"
            except:
                message = "User doesnot exist"
                message_style = "visible"
    content={'msg':message,'msg_style':message_style}
    return render(request,'loginpage.html',content)
    
@authenticated_user
def logout_user(request):
    auth.logout(request)
    return redirect('login_user')
