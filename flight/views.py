from .models import Flight,Reservation
from .serializers import FlightSerializer,ReservationSerializer,StaffFlightSerializer
from rest_framework import viewsets
from .permissions import IsStuffOrReadOnly
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes =(IsStuffOrReadOnly,)
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return StaffFlightSerializer
        else:
            return super().get_serializer_class()
    
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)
    