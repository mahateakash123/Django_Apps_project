

from django.urls import path, re_path
from StudentApp import views

urlpatterns = [
    re_path(r'^$',views.input),
    re_path(r'^comp$',views.compute)
]
