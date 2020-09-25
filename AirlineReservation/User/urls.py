from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
        path('', views.landing),
        path('register', views.register, name="Register"),
        path('login', views.login_view , name="Login"),
        path('logout', views.logout_view, name="Logout")
]
