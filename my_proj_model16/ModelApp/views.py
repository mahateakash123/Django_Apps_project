
from django.shortcuts import render

from ModelApp.models import Emp


# Create your views here.
def emp_input(request):
    emps = Emp.objects.all()
    return render(request,'base.html',{'emps':emps})