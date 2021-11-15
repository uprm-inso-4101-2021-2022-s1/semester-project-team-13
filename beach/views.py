from os import name
from django.shortcuts import render
from .models import Comment, Beach, Rating

# Can map URL's to views.
commentAmount = 3
def display(request, beachName='Jobos'):
    context = {
        'ratings' : Rating.objects.filter(beach__name=beachName),
        'comments': Comment.objects.filter(beach__name=beachName)[:commentAmount], #front-end needs button that modifies the commentAmount variable
        'beaches': Beach.objects.filter(name=beachName),
        'request' : request
        #'comments': Comment.objects.all()[:69],
    }
    return render(request, 'beach/display.html', context)


