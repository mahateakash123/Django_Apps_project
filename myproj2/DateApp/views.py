from django.shortcuts import render
import datetime
from django.http import HttpResponse

def dateapp(request):

    
    today = datetime.datetime.now()

    return HttpResponse("<html><body bgcolor='skyblue'><h1> Current Date:" +str(today)+"</h1></body></html>")


    