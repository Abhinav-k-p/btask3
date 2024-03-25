from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.registeration,name='signup'),
    path('login/',views.loginuser,name='login'),
]