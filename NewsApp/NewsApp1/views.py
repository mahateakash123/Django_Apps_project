from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def input(request):
    return render(request,'base.html')

def political_news_view(request):
    news1="Jagan warning Babu........to shut Everything... "
    news2="IPL to start in the Next week"
    news3="It Rains heavily in the next 48hrs.."
    news4="40% of Indians got Vaccinated"
    news5="Schools reopen to be delayed"
    news6="Python is the Next-Level Language"
    dict1={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,}
    return render(request,'politics.html',context= dict1)

def sport_news_view(request):
    news1="Jagan warning Babu........to shut Everything... "
    news2="IPL to start in the Next week"
    news3="It Rains heavily in the next 48hrs.."
    news4="40% of Indians got Vaccinated"
    news5="Schools reopen to be delayed"
    news6="Python is the Next-Level Language"
    dict1={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5,'news6':news6,}
    return render(request,'politics.html',dict1)
