from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wapper_func

def authenticated_user(view_func):
    def wapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('login_user')
    return wapper_func


def only_superuser(view_func):
    def wapper_func(request,*args,**kwargs):
        if request.user.is_superuser:
            return view_func(request,*args,**kwargs)
        else:
            return HttpResponse('User not allowed here')
    return wapper_func



