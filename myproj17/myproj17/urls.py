
from django.contrib import admin
from django.urls import path
from BookApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.book_app)
]
