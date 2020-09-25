from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
            user.save()
            p = models.Passenger()
            p.user = user
            p.save()
             
            return render(request, "MessagePage.html", {"title": "Success", "message": "You have successfully registered!"})

        else:
            print(user_form.errors)
            return render(request, "FormPage.html", { "title":"Registration" ,"form":forms.UserForm, "error":True, "error_msg":"Form Invalid!" })


    return render(request, "FormPage.html", { "title":"Registration", "form":forms.UserForm, "error":False, "error_msg":"" })


def login_view(request):
    
    if request.user.is_authenticated:
        return render(request, "MessagePage.html", {"title": "Error", "message": "You are already logged in!"})

    if request.method=="POST":
        user_form = forms.UserLoginForm(data = request.POST)

        username = user_form.username
        password = user_form.password

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active():
                return render(request, "MessagePage.html", {"title": "Success", "message": "You have successfully logged in!"})

        return render(request, "FormPage.html", { "title":"Login", "form":forms.UserLoginForm, "error":True, "error_msg":"Invalid credentials" })
    
    return render(request, "FormPage.html", { "title":"Login", "form":forms.UserLoginForm, "error":False, "error_msg":"" })
