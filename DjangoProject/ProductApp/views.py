from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'base.html')

def compute(request):
    pid=request.GET['t1']
    pname=request.GET['t2']
    price=request.GET['t3']
    brand=request.GET['t4']
    qty=request.GET['t5']
    dict1={"prodid":pid,"prodname":pname,"price":price,"brand":brand,"qty":qty}
    return render(request,'base2.html',context=dict1)

