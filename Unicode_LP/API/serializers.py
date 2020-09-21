from account.models import myUser
from CRUD_task.models import App_user
from rest_framework import serializers
from django.contrib.auth.models import auth
from django.core import exceptions
class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = myUser
        fields = ['id','username','email','password','password2']
        extra_kwargs ={
            'password':{
                'style':{'input_type':'password'},
                'write_only':True
                },
            
        }
    def save(self):
        account=myUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if(password!=password2):
            raise serializers.ValidationError({'password':'password does not match'})
        
        account.set_password(password)
        account.save()
        return account

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = App_user
        fields =['Fname','Lname','DOB','pic'] 
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    def validate(self,data):
        username=data.get('username','')
        password=data.get('password','')
        
        if username and password :
            user = auth.authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data['user']=user
                else:
                    msg = 'User is not Active'
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to Login wuth Given credentials'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'Must provide Username and password'
            raise exceptions.ValidationError(msg)

        return data



