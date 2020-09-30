from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
        path('', views.landing, name="Landing"),
        path('flights/', views.flight_full_list, name="FullList"),
        path('flights/add/', views.addFlight, name="AddFlight"),
        path('book/<int:flight_id>', views.bookticket, name="Booking"),
]
