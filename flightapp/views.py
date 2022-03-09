from .models import Flight, Reservation
from .serializers import FlightSerializer
from rest_framework import viewsets


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer