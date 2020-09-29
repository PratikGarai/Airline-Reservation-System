from django.shortcuts import render
from . import forms
from . import models

def landing(request):
    return render(request, "MessagePage.html", {"title" : "Landing", "message":"This is the landing page"});

def bookticket(request, flight_id):
    return render(request, "FormPage.html", {"title":"Booking", "form":forms.TicketForm, "error":True, "error_msg":"Flight id : "+str(flight_id)})
