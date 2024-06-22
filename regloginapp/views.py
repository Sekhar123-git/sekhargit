from django.shortcuts import render
from django.views import View
from .models import Reg
from django.http import HttpResponse
from .forms import RegForm,LoginForm

class Homeview(View):
    def get(self, request):
        return render(request, template_name='home.html')


class RegInput(View):
    def get(self, request):
        rf=RegForm()
        con_dict={"regf":rf}
        return render(request, template_name='reginput.html',context=con_dict)


class RegInsert(View):
    def post(self, request):
        rf1=RegForm(request.POST)
        if  rf1.is_valid():
            r1 = Reg(username=rf1.cleaned_data["username"],
                 password=rf1.cleaned_data["password"],
                 conf_password=rf1.cleaned_data["conf_password"],
                 first_name=rf1.cleaned_data["first_name"],
                 last_name=rf1.cleaned_data["last_name"],
                 emailid=rf1.cleaned_data["emailid"],
                 mobileno=int(rf1.cleaned_data["mobileno"]))
            r1.save()
            return HttpResponse("registration successful")


class LogInput(View):
    def get(self, request):
        lf=LoginForm()
        con_dict={"loginf":lf}
        return render(request, template_name='loginput.html',context=con_dict)


class LoginInVerf(View):
    def post(self, request):
        lf1=LoginForm(request.POST)
        if lf1.is_valid():
            username = lf1.cleaned_data["username"]
            password = lf1.cleaned_data["password"]
        dbuser = Reg.objects.get(username=username, password=password)
        if not dbuser:
            return HttpResponse('login failed')
        else:
            return HttpResponse('login successful')





