from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input(request):

    str1 = '''
        <html>
        <body bgcolor="skyblue">
        <h1> Hello.... welcome to the demo App </h1>
        </body>
        <html>


    '''
    return HttpResponse(str1)
