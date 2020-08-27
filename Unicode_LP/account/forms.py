from django import forms
from .models import myUser
from django.contrib.auth.forms import UserCreationForm

class CreateUser(UserCreationForm):
    class Meta:
        model = myUser
        fields = ['username','email','password1','password2']

       