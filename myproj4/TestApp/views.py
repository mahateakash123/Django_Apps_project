from django.shortcuts import render

from django.http import HttpResponse



def display(request):

    str1 = '''
        <html>
        <body bgcolor="green">
        <h1> Hello.... welcome to the Test App </h1>
        </body>
        <html>


    '''
    return HttpResponse(str1)