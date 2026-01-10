
from django.contrib import admin
from django.urls import path
from ProductApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ProductApp/',views.input),
    path('ProductApp/prod/',views.compute)
]
