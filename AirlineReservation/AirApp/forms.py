from django import forms
from . import models

class FlightFilterForm(forms.Form):
    source = forms.CharField(widget = forms.Select(choices = models.locations))
    destination = forms.CharField(widget = forms.Select(choices = models.locations))
    date = forms.DateField()

class TicketForm(forms.ModelForm):
    class Meta :
        model = models.Ticket
        fields = ('n_passenger',)
