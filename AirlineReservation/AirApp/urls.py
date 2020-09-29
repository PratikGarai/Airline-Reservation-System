from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
        path('', views.landing, name="Landing"),
        path('book/<int:flight_id>', views.bookticket, name="Booking"),
]
