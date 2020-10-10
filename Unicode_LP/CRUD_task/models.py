from django.db import models
from account.models import myUser
# Create your models here.
class App_user(models.Model):
    choice = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
 
    user = models.OneToOneField(myUser,on_delete=models.CASCADE,unique=True)
    pic = models.ImageField(upload_to='pics',default="",blank=True,null=True)
    Fname = models.CharField(max_length=50,default="",blank=True,null=True)
    Lname = models.CharField(max_length=50,default="",blank=True,null=True)
    DOB = models.DateField(auto_now_add=False,auto_created=False,blank=True,null=True)
    gender = models.CharField(max_length=6,choices=choice,blank=True,null=True)
    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.pic.url
        except:
            url=''
        return url

        

class Mail_model(models.Model):
    title=models.CharField(max_length=50)
    sender = models.ForeignKey(myUser,null=True,related_name='sender',on_delete=models.SET_NULL)
    reciver = models.ForeignKey(myUser,null=True,related_name='reciver',on_delete=models.SET_NULL)
    date_Of_Msg = models.DateTimeField(auto_now_add=True)
    seenby_sender = models.BooleanField(default=False)
    seenby_recv = models.BooleanField(default=False)
    def __str__(self):
        return "sender "+str(self.sender)+" rec. "+str(self.reciver)+" ( "+str(self.id)+" )"
    
class Chat_model(models.Model):
    sender = models.ForeignKey(myUser,null=True,related_name='chat_sender',on_delete=models.SET_NULL)
    reciver = models.ForeignKey(myUser,null=True,related_name='chat_reciver',on_delete=models.SET_NULL)
    chat = models.TextField(null=True,blank=True)
    date_Of_chat = models.DateTimeField(auto_now_add=True)
    mail =  models.ForeignKey(Mail_model,null=True,related_name='mail',on_delete=models.CASCADE)
    file = models.FileField(upload_to='files',default="",blank=True,null=True)
    def __str__(self):
        return "sender "+str(self.sender)+" rec. "+str(self.reciver)+" ( "+str(self.id)+" )"    

class contactList(models.Model):
    owner_user = models.ForeignKey(myUser,related_name='owner',on_delete=models.CASCADE)
    contact_user = models.ForeignKey(myUser,related_name='contact_user',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.owner_user) + "->" + str(self.contact_user)