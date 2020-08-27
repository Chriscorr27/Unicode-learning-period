from django.shortcuts import render,redirect
from .forms import CreateUser
# Create your views here.
def create_user(request):
    form = CreateUser()
    #print(form)
    if(request.method == 'POST'):
        form = CreateUser(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')
        
    content={'form':form}
    return render(request,'register_user.html',content)