from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input(request):
    return render(request, 'base.html')


def compute(request):
    p=int(request.GET['t1'])
    t=int(request.GET['t2'])
    r=int(request.GET['t3'])

    si=(p*t*r)/100
    return HttpResponse("<html><body><h1>simple Interest is"+str(si)+"</h1></body></html>")

def about(request):
    return HttpResponse("<html><body><h1>This is a Simple Interest Calculator App developed using Django Framework.</h1></body></html>")