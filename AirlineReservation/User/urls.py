from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
        path('', views.landing),
        path('register', views.register)
        ]
