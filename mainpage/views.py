from django.shortcuts import render
from django.http import HttpResponse
from mainpage.models import Query,Domain
# Create your views here.
def indexpage(request):
    alldomains=Domain.objects.all()
    return render(request,"index.html",{'alldomains':alldomains})
def submitdata(request):
    if request.method=="POST":
        name=request.POST["nameofclient"]
        email=request.POST["emailofclient"]
        cocode=request.POST["ccode"]
        phoneno=request.POST["phonenoofclient"]
        message=request.POST["messagedata"]
        user=Query(name=name,email=email,countrycode=cocode,phone=phoneno,message=message)
        user.save()
        return render(request,"querysubmit.html")
    return HttpResponse("not found")