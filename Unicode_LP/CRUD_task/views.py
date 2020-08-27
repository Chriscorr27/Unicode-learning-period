from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from account.models import myUser
# Create your views here.

def home(request):
    users= App_user.objects.all()
    for user in users:
        print(user.id)
    
    content ={'users':users}
    return render(request,'home.html',content)

def profile_info(request,id):
    user=myUser.objects.get(id=id)
    Profile = App_user.objects.get(user=user)
    content={'user':Profile}
    return render(request,'profile_info.html',content)

def delete_User(request,id):
    user=myUser.objects.get(id=id)
    user.delete()
    return redirect('home')
