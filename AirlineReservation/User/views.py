from django.shortcuts import render
from . import forms
from . import models 

def landing(request):
    
    if not request.user.is_authenticated:
        print("Not logged in")
    else :
        print("logged in")
    return render(request, 'MessagePage.html', {"title" : "Sample Title", "message" : "The sample page"})

def register(request):

    if request.user.is_authenticated:
        return render(request, "MessagePage.html", {"title": "Error", "message": "You are already logged in!"})

    if request.method=="POST":
        user_form = forms.UserForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            p = models.Passenger()
            p.user = user
            p.save()
             
            return render(request, "MessagePage.html", {"title": "Success", "message": "You have successfully registered!"})

        else:
            print(user_form.errors)
            return render(request, "FormPage.html", { "title":"Registration" ,"form":forms.UserForm, "error":True, "error_msg":"Form Invalid!" })


    return render(request, "FormPage.html", { "title":"Registration", "form":forms.UserForm, "error":False, "error_msg":"" })
