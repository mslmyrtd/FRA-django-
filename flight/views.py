from .models import Flight
from .serializers import FlightSerializer
from rest_framework import viewsets
from .permissions import IsStuffOrReadOnly
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes =(IsStuffOrReadOnly,)
    