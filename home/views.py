from django.shortcuts import render
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def home(request):
    return render(request, 'home/home.html')
