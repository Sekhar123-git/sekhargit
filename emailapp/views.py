from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
import random
import requests

class Home(View):
    def get(self, request):
        return render(request,template_name='input.html')
class Send(View):
    def post(self, request):
        subject = 'OTP'
        otp=str(random.randint(10000,99999))
        print(otp)
        From_mail = settings.EMAIL_HOST_USER
        email=request.POST['t1']
        mobno="+91"+request.POST['t2']
        to_list=[email]
        send_mail(subject, otp, From_mail, to_list, fail_silently=False)
        resp = requests.post('http://textbelt.com/text',  {
            'phone':mobno,
             'message':otp,
             'key':"fe37eabe4f8b9dfeb5e2603fdc2eb74f35c57b8nuhTIhoaYe9VTceAfcjM9mIBA",
        })
        print(resp.json())
        return HttpResponse("mail sent successfully")




