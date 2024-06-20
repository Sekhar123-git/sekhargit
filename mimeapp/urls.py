from .views import  htmlview,excelview,xmlview
from django.urls import path
aap_name='mimeapp'
urlpatterns = [
    path('html',htmlview.as_view(), name='htmlview'),
    path('excel',excelview.as_view(), name='excelview'),
    path('xml',xmlview.as_view(), name='xmlview'),
]
