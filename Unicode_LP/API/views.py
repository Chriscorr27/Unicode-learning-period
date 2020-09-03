from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from account.models import myUser
from CRUD_task.models import App_user
@api_view(['GET',])
def apiOverview(request):
    data={
        'List':'userList/',
        'Detail view' : 'userDetail/<str:id>/',
        'Create':'createuser/',
        'Update' : 'upadateProfile/<str:pk>',
        'Delete' : 'deleteUser/<str:pk>',
    }
    return Response(data)

@api_view(['POST',])
def createuser(request):
    serializer=UserSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        user=serializer.save()
        data=serializer.data
        App_user.objects.create(user=user)

    else:
        data=serializer.errors

    return Response(data)
  
        
@api_view(['GET',])
def userList(request):
    users=myUser.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET',])
def userDetail(request,id):
    user=myUser.objects.get(id=id)
    profile = App_user.objects.get(user=user)
    serializer = ProfileSerializer(profile,many=False)
    return Response(serializer.data)

@api_view(['DELETE',])
def deleteUser(request,id):
    user=myUser.objects.get(id=id)
    user.delete()

    return Response("item sucessfully deleted")

@api_view(['POST',])
def upadateProfile(request,id):
    user=myUser.objects.get(id=id)
    profile = App_user.objects.get(user=user)
    serializer = ProfileSerializer(instance=profile,data=request.data)
    data={}
    if serializer.is_valid():
        user=serializer.save()
        data=serializer.data
       

    else:
        data=serializer.errors

    return Response(data)

