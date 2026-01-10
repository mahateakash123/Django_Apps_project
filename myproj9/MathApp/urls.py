

from django.urls import path

from MathApp import views

urlpatterns= [

    path('', views.input),
    path('comp/', views.compute)
]