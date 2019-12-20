from django.shortcuts import render, redirect
from user.models import ResiterModel, ProductModel


# Create your views here.
def saveDetails(request):
    name=request.POST.get("t1")
    passwd=request.POST.get("t2")
    email=request.POST.get("t4")
    contact=request.POST.get("t3")
    status="pending"
    rg=ResiterModel(name=name,password=passwd,emailid=email,contact=contact,status=status).save()
    return render(request,"user_templates/log&reg.html",{"msg":"Admin should be approved"})

def user_home(request):
    name=request.POST.get("t1")
    passwd=request.POST.get("t2")
    try:
     rs=ResiterModel.objects.get(name=name,password=passwd)
     if rs.status=="approved":
        request.session["name"]=rs.name
        request.session["id"] = rs.id
        return render(request,"user_templates/user_home.html")
     elif rs.status=="pending":

        return render(request,"user_templates/log&reg.html",{"msg":"your account is still pending"})
     elif rs.status=="declined":

        return render(request, "user_templates/log&reg.html", {"msg":"your account is declined"})
    except:
        return render(request, "user_templates/log&reg.html", {"msg":"invalid login details"})

def saveSellDetails(request):
    idno=request.POST["t1"]
    name=request.POST["t2"]
    price=request.POST["t3"]
    qnty=request.POST["t4"]
    pinfo=request.POST["t5"]
    image=request.FILES["t6"]
    status="bidding"
    pid=request.session['pid']
    ProductModel(pid=idno,pname=name,bprice=price,pqnty=qnty,pinfo=pinfo,status=status).save()
    return sellProduct(request)
def sellProduct(request):
    ps=ProductModel.objects.all()
    return render(request,"user_templates/sellproduct.html",{"msg":ps})
