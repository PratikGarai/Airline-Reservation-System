from django import forms
from django.contrib.admin import widgets
from . import models

class FlightFilterForm(forms.Form):
    source = forms.CharField(widget = forms.Select(choices = models.locations))
    destination = forms.CharField(widget = forms.Select(choices = models.locations))

class TicketForm(forms.ModelForm):
    class Meta :
        model = models.Ticket
        fields = ('n_passenger',)

class FlightAddForm(forms.ModelForm):
    class Meta :
        model = models.Flight
        fields = '__all__'
