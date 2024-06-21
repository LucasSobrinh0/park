# parking/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Client, ParkingSpot
from .serializers import ClientSerializer, ParkingSpotSerializer
from rest_framework.views import APIView

class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ParkingSpotListView(generics.ListAPIView):
    serializer_class = ParkingSpotSerializer

    def get_queryset(self):
        return ParkingSpot.objects.filter(occupied=False)

class ParkingSpotCreateView(generics.CreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParkingSpotDeleteView(APIView):

    def delete(self, request, pk):
        try:
            parking_spot = ParkingSpot.objects.get(pk=pk)
        except ParkingSpot.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        parking_spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
