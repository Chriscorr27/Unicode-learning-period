from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.apiOverview,name='apihome'),
   path('createuser/',views.createuser,name='createuser-api'),
   path('userList/',views.userList,name='userList-api'),
   path('userDetail/<str:id>/',views.userDetail,name='userDetail-api'),
   path('deleteUser/<str:id>/',views.deleteUser,name='deleteUser-api'),
   path('updateProfile/<str:id>/',views.upadateProfile,name='upadateProfile-api'),
]
