# musicmatch/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('users.urls')),  # Inclure les routes de users sous /api/
    path('admin/', admin.site.urls),
]
