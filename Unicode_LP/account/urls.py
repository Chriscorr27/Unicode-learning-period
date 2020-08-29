from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('create_user',views.create_user,name='create_user'),
   path('register_user',views.register_user,name='register_user'),
   path('login_user',views.login_user,name='login_user'),
   path('logout_user',views.logout_user,name='logout_user'),

]
