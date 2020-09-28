from django.db import models
from User.models import Passenger

locations = [
        ( 'IND', 'India' ),
        ( 'PAK', 'Pakistan' ),
        ( 'USA', 'United States'),
        ( 'GER', 'Germany'),
        ( 'FRA', 'France')
    ]


class Flight(models.Model):

    number = models.CharField(max_length=10, blank = False)
    source = models.CharField(max_length=10, choices = locations)
    destination = models.CharField(max_length=10, choices = locations)
    departure = models.DateTimeField()
    duration = models.DurationField()

class Ticket(models.Model):

    passenger = models.ForeignKey(Passenger, realted_name='tickets', on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, related_name='bookings',on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank = False)
    source = models.CharField(max_length=10, choices = locations)
    destination = models.CharField(max_length=10, choices = locations)
    booked_at = models.DateTimeField(auto_now = True)

