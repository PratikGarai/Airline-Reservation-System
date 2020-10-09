from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
        path('', views.landing, name="Landing"),
        path('flights/', views.flight_full_list, name="FullList"),
        path('flights/add/', views.addFlight, name="AddFlight"),
        path('book/<int:flight_id>', views.bookticket, name="Booking"),
        path('data/flush', views.flush_data , name="Flush"),
        path('profile', views.profile_page, name="Profile"),
        path('cancelTicket/<int:pk>', views.cancelTicket, name="Cancellation"),
        path('deleteFlight/<int:pk>', views.deleteFlight, name="DeleteFlight"),
        path('editFlight/<int:pk>', views.editFlight, name="EditFlight"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
