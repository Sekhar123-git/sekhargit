"""
URL configuration for Project7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from productapp.views import HomeView,InsertInput,InsertView,DisplayView,DeleteView,DeleteInputView,UpdateView,UpdateInputView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('productapp/',HomeView.as_view()),
    path('productapp/insertinput/',InsertInput.as_view()),
    path('productapp/insertinput/insert/',InsertView.as_view()),
    path('productapp/display/',DisplayView.as_view()),
    path('productapp/deleteinput/',DeleteInputView.as_view()),
    path('productapp/deleteinput/delete/',DeleteView.as_view()),
    path('productapp/updateinput/',UpdateInputView.as_view()),
    path('productapp/updateinput/update/',UpdateView.as_view())
]
