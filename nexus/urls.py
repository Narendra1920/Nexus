from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/wifi_scanner/', permanent=False)),  # Redirects root to wifi_scanner
    path('wifi_scanner/', include('wifi_scanner.urls')),  # Include the app URLs
]


