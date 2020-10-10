from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('sendbox',views.send,name='send'),
   path('mail_info/<str:id>',views.mail_info,name='mail_info'),
   path('profile_info/<int:id>',views.profile_info,name='profile_info'),
   path('delete_User/<int:id>',views.delete_User,name='delete_User'),
   path('create_profile/<int:id>',views.create_profile,name='create_profile'),
   path('create_Myprofile/',views.create_Myprofile,name='create_Myprofile'),
   path('Myprofile/',views.Myprofile,name='Myprofile'),
   path('delete_MyUser/',views.delete_MyUser,name='delete_MyUser'),
   path('daseborder/',views.daseborder,name='daseborder'),
   path('create_mail/',views.create_mail,name='create_mail'),
   path('delete_mail/<int:id>',views.delete_mail,name='delete_mail'),




]
