from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    if request.method=="GET":
       x=request.GET["t1"]
       y=request.GET["t2"]
       i=int(x)
       j=int(y)
       k=i+j
       return HttpResponse("the sum is:"+str(k))
    else:
       x = request.POST["t1"]
       y = request.POST["t2"]
       i = int(x)
       j = int(y)
       k = i + j
       return HttpResponse("the sum is:" + str(k))