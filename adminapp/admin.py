from django.contrib import admin
from .models import product
admin.site.register(product)

class productAdmin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'pcost', 'pmfdt', 'pexpdt']
    list_filter = ['pname', 'pmfdt', 'pexpdt']
    class Meta:
        model = product
    admin.site.register(product, productAdmin)

