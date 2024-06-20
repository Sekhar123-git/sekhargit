from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=cyan><h1><center>welcome chandhu</center></h1></body></html>""")
    return res
