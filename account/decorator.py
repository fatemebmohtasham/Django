from django.shortcuts import redirect
from django.http import HttpResponse

def allowed_user(allowed_roles=[]):
  def decorator(view_func):
    def wrapper(request,*args,**kwargs):
      group=None
      if request.user.groups.exists():
        group=request.user.groups.all()[0].name
      if group in allowed_roles:
        return view_func(request,*args,**kwargs)
      else:
        return HttpResponse('you don\'t allow here')  
    return wrapper
  return decorator  






def admin_only(view_func):
  def wrapper(request,*args,**kwargs):
    group=None
    if request.user.groups.exists():
      group=request.user.groups.all()[0].name 
    if group == 'customer':
      return redirect('profile') 
    if group == 'admin':
      return view_func(request,*args,**kwargs)   
  return wrapper