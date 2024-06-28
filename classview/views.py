from django.shortcuts import render
from django.http import HttpResponse
from django.views import  View
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,template_name="home.html")
class add(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        i = int(x)
        j = int(y)
        k = i + j
        return HttpResponse("the sum is:" + str(k))
    def post(self, request):
        x = request.POST["t1"]
        y = request.POST["t2"]
        i = int(x)
        j = int(y)
        k = i + j
        return HttpResponse("the sum is:" + str(k))