from django.shortcuts import render

def landing(request):
    return render(request, "MessagePage.html", {"title" : "Landing", "message":"This is the landing page"});
