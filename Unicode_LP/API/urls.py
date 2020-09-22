from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
   path('',views.APIList,name='apiList'),
   path('userDetail/',userApi.as_view(),name='apihome'),
   path('userDetail/<str:id>/',userDetailApi.as_view(),name='userDetail-api'),
   path('register/',registerApi.as_view(),name='register-user'),
   path('getToken/',getToken.as_view(),name='login-user'),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken')),
  # path('logout/',logoutApi.as_view(),name='logout-user'),
  # path('',views.apiOverview,name='apihome'),
  # path('createuser/',views.createuser,name='createuser-api'),
  # path('userList/',views.userList,name='userList-api'),
  # path('userDetail/<str:id>/',views.userDetail,name='userDetail-api'),
  # path('deleteUser/<str:id>/',views.deleteUser,name='deleteUser-api'),
  # path('updateProfile/<str:id>/',views.upadateProfile,name='upadateProfile-api'),
   
]