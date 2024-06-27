from django.shortcuts import render
from django.views import View
from .models import product

class Displayview(View):
    def get(self, request):
        qs=product.objects.all()
        con_dic={"records":qs}
        return render(request,'display.html',con_dic)
