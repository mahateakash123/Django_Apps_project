
from django.contrib import admin
from django.urls import path
from IntrestApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.input),
    path('Intrest/', views.compute),
    path('About/', views.about),
]
