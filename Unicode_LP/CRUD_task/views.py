from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from account.models import myUser
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import auth
from account.decorator import only_superuser,unauthenticated_user,authenticated_user
from datetime import datetime
from django.utils import timezone
#from dateutil.relativedelta import relativedelta
# Create your views here.
@only_superuser
def daseborder(request):
    users= App_user.objects.all()
    content ={'users':users}
    return render(request,'daseborder.html',content)

@authenticated_user
def send(request):
    form = CreateChat()
    current_time = datetime.now()
    user = request.user
    mails = Mail_model.objects.all().filter(sender=user)
    mail_list=[]
    for mail in mails:
        tdelta = current_time - mail.date_Of_Msg
        #print(tdelta.total_seconds())
        days = tdelta.days
        seconds = tdelta.seconds
        minutes = (seconds//60)%60
        hours=seconds//3600
        time = 'recent'
        if(days>0):
            time=str(days)+"day ago"
            #print(days,"day ago")
        elif(hours>0):
            time=str(hours)+"hour ago"
           # print(hours,"hour ago")
        elif(minutes>0):
            time=str(minutes)+"minute ago"
            #print(minutes,"minute ago")
        elif(seconds>0):
            time=str(seconds)+"second ago"
            #print(seconds,"second ago")
        
        mail_dict={
            'id':mail.id ,
            'title': mail.title,
            'sender': mail.sender,
            'reciver': mail.reciver,
            'seenby_sender': mail.seenby_sender,
            'seenby_recv': mail.seenby_recv,
            'time': time,
        }
        mail_list.append(mail_dict)

    
    indox = False
    content={'mails':mail_list,'indox':indox,'form': form}
    return render(request,'home.html',content)

@authenticated_user
def home(request):
    form = CreateChat()
    current_time = datetime.now()
    user = request.user
    mails = Mail_model.objects.all().filter(reciver=user)
    mail_list=[]
    for mail in mails:
        tdelta = current_time - mail.date_Of_Msg
        #print(tdelta.total_seconds())
        days = tdelta.days
        seconds = tdelta.seconds
        minutes = (seconds//60)%60
        hours=seconds//3600
        time = 'recent'
        if(days>0):
            time=str(days)+"day ago"
            #print(days,"day ago")
        elif(hours>0):
            time=str(hours)+"hour ago"
           # print(hours,"hour ago")
        elif(minutes>0):
            time=str(minutes)+"minute ago"
            #print(minutes,"minute ago")
        elif(seconds>0):
            time=str(seconds)+"second ago"
            #print(seconds,"second ago")
        mail_dict={
            'id':mail.id ,           
            'title': mail.title,
            'sender': mail.sender,
            'reciver': mail.reciver,
            'seenby_sender': mail.seenby_sender,
            'seenby_recv': mail.seenby_recv,
            'time': time,
            
        }
        mail_list.append(mail_dict)

    
    indox = True
    content={'mails':mail_list,'indox':indox,'form': form}
    return render(request,'home.html',content)

@authenticated_user
def create_mail(request):
    if(request.method=='POST'):
        sender=request.user 
        form = CreateChat(request.POST,request.FILES)
        chats= form.save()
        print(chats.file)
        print(chats.chat)
        try:
            recv=myUser.objects.get(username=request.POST['username'])
            title=request.POST['Title']
            #msg = request.POST['message']
            mail=Mail_model(sender=sender,reciver=recv,title=title,seenby_sender=True)
            mail.save()
            chats.sender=sender
            chats.reciver=recv
            chats.mail=mail
            #chats.chat=msg
            chats.save()
        except:
            title=request.POST['Title']
            msg = request.POST['username']
            mail=Mail_model(sender=sender,title=title,seenby_sender=True)
            mail.save()
            #print(mail.reciver)
            chats.sender=sender
            chats.mail=mail
            chats.chat=msg
            chat.save()
        return redirect('home')


@authenticated_user
def mail_info(request,id):
    #print(id)
    form = CreateChat()
    mail = Mail_model.objects.get(id=id)
    user=request.user

    if user==mail.sender or user== mail.reciver:
        if(request.method=='POST'):
            form = CreateChat(request.POST,request.FILES)
            newchat= form.save()
            if(user==mail.sender):
                newchat.sender=user
                newchat.reciver=mail.reciver
                mail.seenby_recv=False
            elif(user==mail.reciver):
                newchat.sender=user
                newchat.reciver=mail.sender
                mail.seenby_sender=False
            newchat.mail=mail
            newchat.save()
            mail.save()
        form = CreateChat()
        if((user==mail.sender and mail.seenby_sender==False) or (user==mail.reciver and mail.seenby_recv==False)):
            if(user==mail.sender):
                mail.seenby_sender=True
            elif(user==mail.reciver):
                mail.seenby_recv=True
        mail.save()
        chats = Chat_model.objects.all().filter(mail=mail)
        chat_infos=[]
        for chat in chats:
            isFile=chat.file!=""
            senderSide= chat.sender == mail.sender
            chat_info={
                'chat': chat.chat,
                'isFile':isFile,
                'senderSide':senderSide,
            }
            if(isFile):
                chat_info['fileUrl']=chat.file.url
            
            chat_infos.append(chat_info)
        mail_dict={
                'id':mail.id ,           
                'title': mail.title,
                'sender': mail.sender,
                'reciver': mail.reciver,
                'seenby_sender': mail.seenby_sender,
                'seenby_recv': mail.seenby_recv,
                'date_Of_Msg':mail.date_Of_Msg
        }
            #print(mail.chat)
        chat_infos.reverse()
        content={'mail':mail_dict,'form':form,'chat_infos':chat_infos}
        return render(request,"mail_info.html",content)
    else:
        return HttpResponse("<h1>YOU ARE NOT ALLOWED SEE THIS MAIL </h1>")

@authenticated_user
def delete_mail(request,id):
    mail = Mail_model.objects.get(id=id)
    user=request.user
    if(mail.sender==user and mail.reciver is None):
        mail.delete()
        return redirect('home')
    else:
        return HttpResponse("<h1>YOU ARE NOT ALLOWED DELETE THIS MAIL </h1>")

@only_superuser
def profile_info(request,id):
    is_user=False
    user=myUser.objects.get(id=id)
    Profile = App_user.objects.get(user=user)
    content={'user':Profile,'is_user':is_user}
    return render(request,'profile_info.html',content)

@only_superuser
def delete_User(request,id):
    user=myUser.objects.get(id=id)
    user.delete()
    return redirect('daseborder')

@only_superuser
def create_profile(request,id):
    #user = request.user
    
    user = myUser.objects.get(id=id)
    app = App_user.objects.get(user=user)
    form = CreateProfile(instance=app)
    message=""
    message_style="invisible"
    #print(id)
    #print(form)
    if request.method == "POST":
        form = CreateProfile(request.POST,request.FILES,instance=app)
        
        if form.is_valid():
            #print(form.cleaned_data['user'])
            
            #print(users.Fname)
            if form.cleaned_data['gender'] is not None:
                form.save()
                return redirect('daseborder')
            else:
                message = "gender should be be specified"
                message_style = "visible"
    content={'form':form,'message':message,'msg_style':message_style}
    return render(request,'create_profile.html',content)

@authenticated_user   
def create_Myprofile(request):
    user = request.user
    app = App_user.objects.get(user=user)
    form = CreateProfile(instance=app)
    message=""
    message_style="invisible"
    #print(id)
    #print(form)
    if request.method == "POST":
        form = CreateProfile(request.POST,request.FILES,instance=app)
        
        if form.is_valid():
            #print(form.cleaned_data['user'])
            
            #print(users.Fname)
            if form.cleaned_data['gender'] is not None:
                form.save()
                return redirect('home')
            else:
                message = "gender should be be specified"
                message_style = "visible"
    content={'form':form,'message':message,'msg_style':message_style}
    return render(request,'create_profile.html',content)
@authenticated_user
def Myprofile(request):
    is_user=True
    user=request.user
    Profile = App_user.objects.get(user=user)
    content={'user':Profile,'is_user':is_user}
    return render(request,'profile_info.html',content)

@authenticated_user
def delete_MyUser(request):
    user=request.user
    
    auth.logout(request)
    user.delete()
    return redirect('login_user')
