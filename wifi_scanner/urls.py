from django.urls import path
from . import views

urlpatterns = [
    path('', views.wifi_signal_strength_view, name='wifi_scanner'),
]