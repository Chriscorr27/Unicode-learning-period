from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from account.models import myUser
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import auth
from account.decorator import only_superuser,unauthenticated_user,authenticated_user
# Create your views here.
@only_superuser
def daseborder(request):
    users= App_user.objects.all()
    content ={'users':users}
    return render(request,'daseborder.html',content)

@authenticated_user
def home(request):
    content={}
    return render(request,'home.html',content)
    
@only_superuser
def profile_info(request,id):
    is_user=false
    user=myUser.objects.get(id=id)
    Profile = App_user.objects.get(user=user)
    content={'user':Profile,'is_user':is_user}
    return render(request,'profile_info.html',content)

@only_superuser
def delete_User(request,id):
    user=myUser.objects.get(id=id)
    user.delete()
    return redirect('daseborder')

@only_superuser
def create_profile(request,id):
    #user = request.user
    
    user = myUser.objects.get(id=id)
    app = App_user.objects.get(user=user)
    form = CreateProfile(instance=app)
    message=""
    message_style="invisible"
    #print(id)
    #print(form)
    if request.method == "POST":
        form = CreateProfile(request.POST,request.FILES,instance=app)
        
        if form.is_valid():
            #print(form.cleaned_data['user'])
            
            #print(users.Fname)
            if form.cleaned_data['gender'] is not None:
                form.save()
                return redirect('daseborder')
            else:
                message = "gender should be be specified"
                message_style = "visible"
    content={'form':form,'message':message,'msg_style':message_style}
    return render(request,'create_profile.html',content)

@authenticated_user   
def create_Myprofile(request):
    user = request.user
    app = App_user.objects.get(user=user)
    form = CreateProfile(instance=app)
    message=""
    message_style="invisible"
    #print(id)
    #print(form)
    if request.method == "POST":
        form = CreateProfile(request.POST,request.FILES,instance=app)
        
        if form.is_valid():
            #print(form.cleaned_data['user'])
            
            #print(users.Fname)
            if form.cleaned_data['gender'] is not None:
                form.save()
                return redirect('home')
            else:
                message = "gender should be be specified"
                message_style = "visible"
    content={'form':form,'message':message,'msg_style':message_style}
    return render(request,'create_profile.html',content)
@authenticated_user
def Myprofile(request):
    is_user=True
    user=request.user
    Profile = App_user.objects.get(user=user)
    content={'user':Profile,'is_user':is_user}
    return render(request,'profile_info.html',content)

@authenticated_user
def delete_MyUser(request):
    user=request.user
    
    auth.logout(request)
    user.delete()
    return redirect('login_user')
