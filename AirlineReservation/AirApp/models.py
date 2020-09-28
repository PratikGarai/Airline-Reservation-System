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
    capacity = models.PositiveIntegerField()
    vacancy = models.PositiveIntegerField(blank=True,default=None)
    departure = models.DateTimeField()
    reach = models.DateTimeField()

    def vacancy_change(self, n):
        self.vacancy += n
        self.save()

    def save(self):
        if self.vacancy==None:
            self.vacancy = self.capacity
        super().save()

class Ticket(models.Model):

    passenger = models.ForeignKey(Passenger, related_name='tickets', on_delete=models.CASCADE)
    n_passenger = models.PositiveIntegerField()
    flight = models.ForeignKey(Flight, related_name='bookings',on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank = False)
    booked_at = models.DateTimeField(auto_now = True)

    def save(self):
        self.flight.vacancy_change(-self.n_passenger)
        super().save()

    def delete(self):
        self.flight.vacancy_change(self.n_passenger)
        super().delete()
