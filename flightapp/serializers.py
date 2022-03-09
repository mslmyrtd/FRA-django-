from rest_framework import serializers
from .models import Flight,Reservation,Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        models=Flight
        fields=(
            "id",
            "flightNumber",
            "operatingAirlines",
            "departureCity",
            "arrivalCity",
            "dateOfDeparture",
            "estimatedTimeOfDeparture",
        )

   