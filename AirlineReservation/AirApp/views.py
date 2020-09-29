from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

def landing(request):
    return render(request, "FormPage.html", {"title":"Welcome!", "form":forms.FlightFilterForm, "error":False, "error_msg":""})

def flight_full_list(request):
    return render(request, "FlightList.html", { "flight_list": models.Flight.objects.all() })

@login_required
def bookticket(request, flight_id):
    return render(request, "FormPage.html", {"title":"Booking", "form":forms.TicketForm, "error":True, "error_msg":"Flight id : "+str(flight_id)})
