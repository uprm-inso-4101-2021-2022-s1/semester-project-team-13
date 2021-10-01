from os import name
from django.shortcuts import render
from .models import Comment, Beach
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.
commentAmount = 3
def display(request, beachName='Jobos'):
    context = {
        'comments': Comment.objects.filter(beach__name=beachName)[:commentAmount], #front-end needs button that modifies the commentAmount variable
        'beaches': Beach.objects.filter(name=beachName),
        #'comments': Comment.objects.all()[:69],
    }
    return render(request, 'beach/display.html', context)
