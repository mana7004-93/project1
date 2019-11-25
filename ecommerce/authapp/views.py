import json
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import http
from .models import Register
from .forms import LoginForm
from .forms import RegForm
import random
import http.client
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        reg=RegForm(request.POST)
        if reg.is_valid():
            x=otp_send(request)
            if x:
                return render(request,'otp_input.html')
            else:
                return render(request,'signup.html')
        else:
            return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def otpvalidation(request):
    newotp=request.POST['otp']
    oldotp=request.POST['otp']
    if newotp==oldotp:
        form=RegForm(request.session['details'])
        new_user=User.objects.create_user(username=request.session["uname"],password=request.session['pwd'])
        new_user.save()
        form.save()
        login(request,new_user)
        return render(request,'price.html')
    else:
        return render(request,'otp_input.html')

def otp_send(requset):
    ot = str(random.randint(100000, 999999))
    phno=requset.POST["phno"]
    requset.session["uname"]=requset.POST["uname"]
    requset.session["pwd"] = requset.POST["pwd"]
    # subject="registation otp"
    requset.session["details"]=requset.POST
    requset.session["otp"]=ot
    conn=http.client.HTTPConnection("api.msg91.com")
    payload = "{\"sender\":\"QWERTY\", \"route\": \"4\", \"country\": \"91\", \"sms\": [{\"message\":\"" + ot + "\", \"to\": [\"" + phno + "\"]}]}"
    headers={'authkey':"300283ACV3o60m5daee5de",
             'content-type':"application/json"}
    conn.request("POST","/api/v2/sendsms?country=91&sender=&route=&mobiles=&authkey=&encrypt=&message=&flash=&unicode=&schtime=&aferminute=&response=&campaign=",payload,headers)
    data=conn.getresponse()
    res = json.loads(data.read().decode("UTF-8"))
    print(res)
    if res["type"] == "success":
        return True
    else:
        return False

@login_required
def login(request):
    return render(request,'price.html')

def my_logout(request):
    logout(request)
    return render(request,'index.html')

