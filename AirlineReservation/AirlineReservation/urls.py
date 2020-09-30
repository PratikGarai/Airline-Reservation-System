from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('User.urls'), name="User"),
    path('', include('AirApp.urls'), name="App")
]

from . import settings
from django.contrib.staticfiles.urls import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
