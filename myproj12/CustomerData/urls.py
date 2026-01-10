
from django.urls import path
from CustomerData import views

urlpatterns={
    
    path('',views.input),
    path('cust/', views.display)
}