from django.contrib import admin
from .models import Product, Stock


# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display = ['pid', 'pname', 'pcat', 'pcost', 'pmfdt', 'pexpdt', 'discount']
    list_filter = ['pcat', 'pmfdt', 'pexpdt']

    class meta:
        model = Product


admin.site.register(Product, productadmin)


class Stockadmin(admin.ModelAdmin):
    list_display = ['prodid', 'tot_qty', 'last_update', 'next_update']
    list_filter = ['prodid']

    class meta:
        model = Stock


admin.site.register(Stock, Stockadmin)
