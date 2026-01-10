
from django.urls import path,include
from DynamicDateApp import views
urlpatterns = [

    path('',views.input)
]