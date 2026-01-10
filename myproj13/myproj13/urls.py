
from django.contrib import admin
from django.urls import path
from StaticApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('StaticApp/', views.input)
]
