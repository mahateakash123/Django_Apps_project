

from django.shortcuts import render
import datetime

def input(request):
    dt = datetime.datetime.now()
    datetime1 = {'date':dt}
    return render(request, 'base1.html', context=datetime1)
