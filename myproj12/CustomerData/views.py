from django.shortcuts import render

# Create your views here.

def input(request):
    return render(request,'base1.html')

def display(request):
    cname=request.GET['t1']
    caccno = int(request.GET['t2'])
    branch = request.GET['t3']
    balance = int(request.GET['t4'])
    dict1 = {'cname':cname,'caccno':caccno,'branch':branch,'balance':balance}
    return render(request, 'base2.html',context=dict1)
