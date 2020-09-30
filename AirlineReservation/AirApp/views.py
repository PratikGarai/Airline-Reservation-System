from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import forms
from . import models

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
                if flight.source==flight.destination :
                    errors.append("Source and destination are the same")
                if flight.capacity==0:
                    errors.append("Capacity of flight is 0")
                if flight.vacancy>flight.capacity:
                    errors.append("Vacancy in flight is more than capacity")
                if flight.vacancy==0:
                    errors.append("Flight capacity is 0")
                if flight.departure>=flight.reach:
                    errors.append("Depature earlier than reahing time")
            else:
                return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":False, "error_msg":["Corrupted form"]})

            if len(errors)>0:
                return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":False, "error_msg":errors})

            flight.save()
            return redirect("/flights")

        return render(request, "FormPage.html", {"title":"Add Flight!", "form":forms.FlightAddForm, "error":False, "error_msg":[]})
    else:
        return render(request, "MessagePage.html", {"title":"Unauthorised!", "message":"You are not authorised to view this page!"}) 

@login_required
def bookticket(request, flight_id):
    return render(request, "FormPage.html", {"title":"Booking", "form":forms.TicketForm, "error":False, "error_msg":[]})
