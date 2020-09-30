from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('User.urls'), name="User"),
    path('', include('AirApp.urls'), name="App")
]
