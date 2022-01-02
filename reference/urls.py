from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from reference import views

urlpatterns = [
    path('', views.home,name="home"),
    path('javascript', views.javascript,name="javascript"),
    path('python',views.python,name="python"),
]
