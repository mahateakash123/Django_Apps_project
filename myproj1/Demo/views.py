from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    str = """<html>
            <body bgcolor="Red" text="yellow">
        <h1> my first django project </h1>
        </body>
        </html>"""
    
    return HttpResponse(str)