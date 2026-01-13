
from django.contrib import admin
from django.urls import path
from ModelApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.emp_input)
]
