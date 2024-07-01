from django.shortcuts import render
from django.views import View
from .models import Product

class Displayview(View):
    def get(self, request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,'display.html',con_dic)
