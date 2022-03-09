from django.db import models

# Create your models here.
class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=25)
    departureCity=models.CharField(max_length=30)
    arrivalCity=models.CharField(max_length=30)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()
    
    def __str__(self):
        return f'{self.flightNumber}- {self.departureCity}-{self.arrivalCity}'
    
    
class Passenger(models.Model):
    firstName=models.Charfield(max_length=40)
    lastName=models.Charfield(max_length=30)
    email=models.Emailfield()
    phoneNumber = models.IntegerField()
    updateDate =models.DateTimeField(auto_now=True)
    createDate =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    