from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import forms
from . import models
from User.models import Passenger
import time


def landing(request):
    return render(request, "FormPage.html", {"title":"Welcome!", "form":forms.FlightFilterForm, "error":False, "error_msg":[]})

def flight_full_list(request):
    return render(request, "FlightList.html", { "flight_list": models.Flight.objects.all() })


@login_required
def addFlight(request):
    if request.user.is_superuser :
        if request.method=='POST':
            flight = forms.FlightAddForm(data = request.POST)
            errors = []

            if flight.is_valid():
                # custom validation begins
                if flight.cleaned_data['source']==flight.cleaned_data['destination'] :
                    errors.append("Source and destination are the same")
                if flight.cleaned_data['capacity']==0:
                    errors.append("Capacity of flight is 0")
                if flight.cleaned_data['vacancy']>flight.cleaned_data['capacity']:
                    errors.append("Vacancy in flight is more than capacity")
                if flight.cleaned_data['vacancy']==0:
                    errors.append("Flight capacity is 0")
                if flight.cleaned_data['departure']>=flight.cleaned_data['reach']:
                    errors.append("Depature earlier than reahing time")
            else:
                return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":True, "error_msg":["Corrupted form"]})

            if len(errors)>0:
                return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":True, "error_msg":errors})

            flight.save().save()
            return redirect("/flights/")

        return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":False, "error_msg":[]})
    else:
        return render(request, "MessagePage.html", {"title":"Unauthorised!", "message":"You are not authorised to view this page!"}) 


@login_required
def bookticket(request, flight_id):
    if request.method=='POST':
        flight = models.Flight.objects.all().filter(pk=flight_id)[0]
        ticket_form = forms.TicketForm(request.POST)
        if ticket_form.is_valid() and flight:
            n_booking = ticket_form.cleaned_data['n_passenger']
            if n_booking>flight.vacancy:
                return render(request, "MessagePage.html", {"title":"Error", "message":"Number of bookings exceeds vacancy!"})
            passenger = Passenger.objects.all().filter(user = request.user)[0]
            ticket = models.Ticket()
            ticket.passenger = passenger
            ticket.n_passenger = n_booking
            ticket.flight = flight
            ticket.number = time.time()
            ticket.save()
            return render(request, "MessagePage.html", {"title":"Booked", "message":"Your ticket has been succesfully booked"})
        else:
            return render(request, "MessagePage.html", {"title":"Error!", "message":"Form Corrupted"})
    return render(request, "FormPage.html", {"title":"Booking", "form":forms.TicketForm, "error":False, "error_msg":[]})


@login_required
def flush_data(request):
    if request.user.is_superuser:
        models.Flight.objects.all().delete()
        models.Ticket.objects.all().delete()
        return redirect("/flights/")
    else:
        return render(request, "MessagePage.html", {"title":"Unauthorised!", "message":"You are not authorised to view this page!"}) 


@login_required
def profile_page(request):
    if request.user.is_superuser:
        return redirect('admin/')
    else:
        passenger = Passenger.objects.all().filter(user=request.user)[0]
        if passenger:
            return render(request, "ProfilePage.html", {"title":"Your Profile", "passenger" : passenger})
        else:
            return render(request, "MessagePage.html", {"title":"Not found", "message":"User not found"})
