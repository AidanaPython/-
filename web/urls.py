from django.contrib import admin
from django.urls import path
from website.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="home")
]
