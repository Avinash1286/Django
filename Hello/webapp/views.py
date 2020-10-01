from django.shortcuts import render, HttpResponse
from .models import Phone
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'var1':'Google',
        'var2':'Funny'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Phone(name=name,phone=phone,email=email,desc=message,date=datetime.now())
        contact.save()
        messages.success(request,"Your Details has been submitted.")
    return render(request,'contact.html')