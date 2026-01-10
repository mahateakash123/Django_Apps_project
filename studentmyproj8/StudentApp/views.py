from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'base.html')


def compute(request):
    name=request.GET['t1']
    rollno=int(request.GET['t2'])
    branch=request.GET['t3']
    college=request.GET['t4']
    maths= int(request.GET['t5'])
    chemistry = int(request.GET['t6'])
    physics = int(request.GET['t7'])
    total = maths + chemistry + physics
    avg = total/3
    return HttpResponse("<html><body bgcolor='yellow'><h2> STUDENT NAME:"+name+
                        "<br>STUDENT ROLLNO:"+str(rollno)+
                         "<br>STUDENT BRANCH:" + branch +
                         "<br>STUDENT COLLEGE:" + college +
                         "<br>STUDENT MATHS:" + str(maths) +
                        "<br>STUDENT CHEMISTRY:" + str(chemistry) +
                        "<br>STUDENT PHYSICS:" + str(physics) +
                        "<br>TOTAL:"+ str(total) +
                        "<br> AVG:"+str(avg)+"</h2></body></html>")

