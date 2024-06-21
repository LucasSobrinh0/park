# parking/serializers.py
from rest_framework import serializers
from .models import Client, ParkingSpot

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = ['id', 'spot_number', 'occupied', 'client']
