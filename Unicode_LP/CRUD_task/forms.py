from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
class CreateProfile(forms.ModelForm):
   # name=forms.CharField()
    class Meta:
        model = App_user
        fields = '__all__'
        exclude=['user']

class CreateChat(forms.ModelForm):
   # name=forms.CharField()
    class Meta:
        model = Chat_model
        fields = ['file','chat']

    