from django.shortcuts import render
from .models import Students

def index(request):
    data = Students.objects.all()
    return render(request,'home.html',{'data': data})

