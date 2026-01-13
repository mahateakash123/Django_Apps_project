from django.shortcuts import render
from BookApp.models import Book


def book_app(request):
    book = Book.objects.all()
    return render(request,'base.html',{'book':book})



