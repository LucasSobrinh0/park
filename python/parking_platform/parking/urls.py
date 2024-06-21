# parking/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('parking-spots/', ParkingSpotListView.as_view(), name='parking-spot-list'),
    path('parking-spots/create/', ParkingSpotCreateView.as_view(), name='parking-spot-create'),
    path('parking-spots/<int:pk>/delete/', ParkingSpotDeleteView.as_view(), name='parking-spot-delete'),
]
