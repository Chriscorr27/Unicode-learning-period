from django.core.management.base import BaseCommand,CommandError
from CRUD_task.models import App_user
from account.models import myUser
class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('--delete',help='id to delete user')
        parser.add_argument('--userDetail',help='id to see user info')
        parser.add_argument('--users',action='store_true')

        #parser.add_argument('--users')
    def handle(self,*agrs,**options):
        #print("command : Mycommand")
        #print(f'command: {options["command"]}')
        if((options['users']) and (options['userDetail'] is None) and (options['delete'] is None) ):
            users = myUser.objects.all()
            print("  All Users  ")
            for user in users:
                print(f"id : {user.id}\nusername : {user.username}\nemail : {user.email}\n")
        elif((options['userDetail'] is not None) and (options['delete'] is None) and (options['users']==False)):
            users = myUser.objects.all().filter(id=options['userDetail'])
            
            #print(user.exists())
            if(users.exists()):
                user = myUser.objects.get(id=options['userDetail'])
                userInfo = App_user.objects.get(user=user)
                #userInfos = App_user.objects.all()
                print("   user Info   ")
                print(f"id : {user.id}")
                print(f"username : {user.username}")
                print(f"email : {user.email}")
                print(f"Name : {userInfo.Fname} {userInfo.Lname}")
                print(f"DOB : {userInfo.DOB}")
                print(f"gender : {userInfo.gender}")
             
            else:
                print("User Not Exist")

        elif((options['userDetail'] is None) and (options['delete'] is not None) and (options['users']==False)):
           # print(f"Delete User  {options['delete']}")
            users = myUser.objects.all().filter(id=options['delete'])
            #print(user.exists())
            if(users.exists()):
                for user in users:
                    user.delete()
             
            else:
                print("User Not Exist")
        else:
            raise CommandError("Invalid Commands")