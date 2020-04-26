from django.shortcuts import render
from django.http import HttpResponse
from .models import notice
# Create your views here.

def home(request):
    notices = notice.objects.all()
    return render(request,'home.html',{
        'notice':notices,
    })

   