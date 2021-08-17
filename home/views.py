from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from home.models import Coontact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable1":"this is sent",
        "variable2" : "this is sent"
    }
    messages.success(request,"this is a text message")

    
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Coontact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, ' Your Profile details has been updated!')
    return render(request,'contact.html')