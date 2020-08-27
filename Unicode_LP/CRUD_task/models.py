from django.db import models
from account.models import myUser
# Create your models here.
class App_user(models.Model):
    choice = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
 
    user = models.OneToOneField(myUser,on_delete=models.CASCADE,unique=True)
    pic = models.ImageField(upload_to='pics',null=True)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    DOB = models.DateField(auto_now_add=False,auto_created=False)
    gender = models.CharField(max_length=6,choices=choice)
    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.pic.url
        except:
            url=''
        return url

        

class Chat_model(models.Model):
    sender = models.ForeignKey(myUser,null=True,related_name='sender',on_delete=models.SET_NULL)
    reciver = models.ForeignKey(myUser,null=True,related_name='reciver',on_delete=models.SET_NULL)
    chat = models.TextField()
    date_Of_Msg = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    

class contactList(models.Model):
    owner_user = models.ForeignKey(myUser,related_name='owner',on_delete=models.CASCADE)
    contact_user = models.ForeignKey(myUser,related_name='contact_user',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner_user) + "->" + str(self.contact_user)