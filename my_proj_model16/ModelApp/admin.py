from django.contrib import admin
from ModelApp import models
from ModelApp.models import Emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','sal','sex','dno']

admin.site.register(Emp,EmpAdmin)