

from django.contrib import admin
from django.urls import path, re_path
from DemoApp import views as v1
from TestApp import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^demo/$', v1.input),
    re_path(r'^test/$', v2.display)
]
