from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greeting/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('another/', views.another, name='another')
]