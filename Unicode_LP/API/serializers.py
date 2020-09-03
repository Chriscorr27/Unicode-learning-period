from account.models import myUser
from CRUD_task.models import App_user
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = myUser
        fields = ['username','email','password','password2']
        extra_kwargs ={
            'password':{'write_only':True}
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
        fields = ['Fname','Lname','DOB','gender']

    
