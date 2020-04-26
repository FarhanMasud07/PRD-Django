from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*arg,**kwargs):
        if request.user.is_authenticated:
            return redirect('admindashboard')
        else:
            return view_func(request,*arg,**kwargs)
    return wrapper_func    

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request,*arg,**kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:    
#                 return view_func(request,*arg,**kwargs)    
#             else:
#                 return HttpResponse('you are not authorized to view this page')    
#         return wrapper_func
#     return decorator   


def admin_only(view_func):
    def wrapper_func(request,*arg,**kwargs):
        group = None
        
        group = request.user.groups.all()[0].name
          
        if group == 'customers':    
            return redirect('customerdashboard')    
        if group == 'admins':
            return view_func(request,*arg,**kwargs)    
    return wrapper_func


def customer_only(view_func):
    def wrapper_func(request,*arg,**kwargs):
        group = None
        group = request.user.groups.all()[0].name   
        if group == 'admins':    
            return redirect('admindashboard')    
        if group == 'customers':
            return view_func(request,*arg,**kwargs)    
    return wrapper_func    
