from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import product

class HomeView(View):
    def get(self, request):
        return render(request,template_name="home.html")

class InsertInput(View):
    def get(self, request):
        return render(request,template_name="productinput.html")
class InsertView(View):
    def get(self, request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res=HttpResponse("product inserted successfully")
        return res

class DisplayView(View):
    def get(self, request):
            qs=product.objects.all()
            con_dic={"records":qs}
            return render(request,template_name="display.html",context=con_dic)




class DeleteInputView(View):
    def get(self, request):
        return render(request,template_name="deleteinput.html")

class DeleteView(View):
    def get(self, request):
        p_id=int(request.GET["t1"])
        prod=product.objects.filter(pid=p_id)
        prod.delete()
        res=HttpResponse("product deleted successfully")
        return res

class UpdateInputView(View):
    def get(self, request):
        return render(request, template_name="updateinput.html")
class UpdateView(View):
    def post(self, request):
        p_id=int(request.POST["t1"])
        p_name=request.POST["t2"]
        p_cost=float(request.POST["t3"])
        p_mfdt=request.POST["t4"]
        p_expdt=request.POST["t5"]
        prod=product.objects.get(pid=p_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        res=HttpResponse("product updated successfully")
        return res


