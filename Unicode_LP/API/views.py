from django.shortcuts import render
from rest_framework import status,generics,mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from account.models import myUser
from CRUD_task.models import App_user
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import auth
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class userApi(APIView):
    serializer_class = UserSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request):
        users=myUser.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status=200)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        #data={}
        if serializer.is_valid():
            user=serializer.save()
            data=serializer.data
            App_user.objects.create(user=user)
            return Response(serializer.data,status=201) 
        return Response(serializer.errors,status=400)


class userDetailApi(APIView):
    serializer_class = ProfileSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request,id=None):
        user=myUser.objects.get(id=id)
        profile = App_user.objects.get(user=user)
        serializer = ProfileSerializer(profile,many=False)
        return Response(serializer.data,status=200)

    def put(self,request,id=None):
        user=myUser.objects.get(id=id)
        profile = App_user.objects.get(user=user)
        serializer = ProfileSerializer(instance=profile,data=request.data)
        #data={}
        if serializer.is_valid():
            user=serializer.save()
            return Response(serializer.data,status=201) 
        return Response(serializer.errors,status=400)
    def delete(self,request,id=None):
        
        user=myUser.objects.get(id=id)
        user.delete()
        return Response("item sucessfully deleted",status=200)


#Authenication

class registerApi(APIView):
    serializer_class = UserSerializer
    def post(self,request):
        if request.user.is_authenticated :
            data ={
                'Error': 'Login User Cannot Register'
            }
            return Response(data,status=400)
        else:
            serializer=UserSerializer(data=request.data)
            #data={}
            if serializer.is_valid():
                user=serializer.save()
                data=serializer.data
                App_user.objects.create(user=user)
                data=serializer.data
                data['Login']= 'api/login/'
                return Response(data,status=201) 
            return Response(serializer.errors,status=400)

class getToken(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
            serializer=LoginSerializer(data=request.data)
            #data={}
            if serializer.is_valid(raise_exception=True):
                authuser = serializer.validated_data['user'] 
               # auth.login(request,authuser)
                token,created=Token.objects.get_or_create(user=authuser)
                data=serializer.data
                data['Token']= token.key
                return Response(data,status=201) 
            return Response(serializer.errors,status=400)
'''
class logoutApi(APIView):
    
    permission_classes=[IsAuthenticated]
    def get(self,request):
        #print(request.user.is_authenticated)
        if request.user.is_authenticated:
            auth.logout(request)
            print(request.user)
            #data={'user':request.user}
            return Response(status=204)
        else:
            data ={
                'Error': 'user is not authenticated'
            }
            return Response(data,status=400)
'''
#APIVIW by function

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
def APIList(request):  
    data={
        'Users':'api/userDetail/',
        'User Profile' : 'api/userDetail/<str:id>/',
        'Register User':'api/register/',
        'Login User' : 'api/login/',
        'Logout User' : 'api/logout/',
    }
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

    



