from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('profile_info/<int:id>',views.profile_info,name='profile_info'),
   path('delete_User/<int:id>',views.delete_User,name='delete_User'),

]
