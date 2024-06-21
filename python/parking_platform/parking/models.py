# parking/models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)

class ParkingSpot(models.Model):
    spot_number = models.IntegerField(unique=True)
    occupied = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
