from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def calculate(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    operation=request.POST["op"]
    i=int(x)
    j=int(y)
    if operation=="Add":
        res= i + j
        return HttpResponse("the sum is:"+str(res))
    elif operation=="sub":
        res = i - j
        return HttpResponse("the sub is:" + str(res))
    elif operation=="mul":
        res = i * j
        return HttpResponse("the mul is:" + str(res))
    else:
        res = i / j
        return HttpResponse("the div is:" + str(res))
