from django.urls import path
from .import views
from cart.urls import urlpatterns
# Paths for the Fresh Fruits App

app_name = 'fruitsApp'


urlpatterns = [
    path('', views.home, name='fruits-homepage'),
    path(r'media/', views.home, name='images'),
]