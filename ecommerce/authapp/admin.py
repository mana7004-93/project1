from django.contrib import admin
from .models import Register

class Regadmin(admin.ModelAdmin):
    list_display = ('fname', 'phno', 'email', 'uname', 'pwd', 'cpwd')


admin.site.register(Register,Regadmin)
