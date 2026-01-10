
from django.contrib import admin
from django.urls import path,re_path
from NewsApp1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^NewsApp1$',views.input),
    re_path(r'^politics$',views.political_news_view),
    re_path(r'^sport$',views.sport_news_view),
    

]
