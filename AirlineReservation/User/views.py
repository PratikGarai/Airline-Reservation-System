from django.shortcuts import render

def landing(request):
    
    if not request.user.is_authenticated:
        print("Not logged in")
    else :
        print("logged in")
    return render(request, 'MessagePage.html', {"title" : "Sample Title", "message" : "The sample page"})

def register(request):

    if request.user.is_authenticated:
        return render(request, "MessagePage.html", {"title": "Error", "message": "You are already logged in!"})
