
from django.urls import path
from AddApp import views


urlpatterns = [

    path('',views.input),
    path('add/',views.add)
]