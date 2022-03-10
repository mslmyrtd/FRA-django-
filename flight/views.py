from .models import Flight,Reservation
from .serializers import FlightSerializer,ReservationSerializer
from rest_framework import viewsets
from .permissions import IsStuffOrReadOnly
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes =(IsStuffOrReadOnly,)
    
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
    