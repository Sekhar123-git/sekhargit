from django.shortcuts import render
from django.views import View
from .models import Reg
from django.http import HttpResponse

class Home(View):
    def get(self, request):
        return render(request,template_name='home.html')
class RegInput(View):
    def get(self, request):
        return render(request,template_name='reginput.html')

class RegInsert(View):
    def post(self, request):
        r1=Reg(username = request.POST['t1'],
               password = request.POST['t2'],
               conf_password=request.POST['t3'],
               first_name=request.POST['t4'],
               last_name=request.POST['t5'],
               emailid=request.POST['t6'],
               mobileno=int(request.POST['t7']))
        r1.save()
        return HttpResponse("registration successful")
class LogInput(View):
    def get(self, request):
        return render(request,template_name='logininput.html')

class LoginInVerf(View):
    def post(self, request):
        user=request.POST['t1']
        password=request.POST['t2']
        dbuser = Reg.objects.get(username=user,password=password)
        if not dbuser:
            return HttpResponse('login failed')
        else:
            return HttpResponse('login successful')