from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.
from badmin.sms import sendSMS
from user.models import ResiterModel

def saveDetails(request):
    uname=request.POST.get("t1")
    passwd=request.POST.get("t2")
    if uname=="thrilok" and passwd=="THRILOK":
        return redirect('admin_home')
    else:
        messages.error(request,"invalid login details")
        return redirect('admin_login')
def pending_reg(request):
 reg=ResiterModel.objects.filter(status="pending")
 return render(request,"badmin_templates/pending_reg.html",{"msg":reg})

def approved_reg(request):
   result=ResiterModel.objects.filter(status="approved")
   return render(request,"badmin_templates/approved_reg.html",{"msg":result})
def declined_reg(request):
    result=ResiterModel.objects.filter(status="declined")
    return render(request,"badmin_templates/declined_reg.html",{"msg":result})
def approved(request):
    x=request.POST["t1"]
    result=ResiterModel.objects.filter(name=x)
    name=""
    contact=""
    for x in result:
        name=x.name
        contact=x.contact
    result.update(status="approved")
    mess='Hello Mr/Miss :'+ name +'your registration was approved '
    x=sendSMS(str(contact),mess)
    print(x)
    return redirect('approved_reg')

def declined(request):
    x=request.POST.get("t2")
    result = ResiterModel.objects.filter(name=x)
    name = ""
    contact = ""
    for x in result:
        name = x.name
        contact = x.contact
    result.update(status="approved")
    mess = 'Hello Mr/Miss :' + name + 'your registration was declined '
    x = sendSMS(str(contact), mess)
    print(x)
    return redirect('declined_reg')

def logout(request):
    return redirect('home')