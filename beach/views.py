from os import name
from django.shortcuts import render
from .models import Comment, Beach, Rating
from django.http import HttpResponse
# Can map URL's to views.
commentAmount = 3

def display(request, beachName='Jobos'):
    context = {
        'comments': Comment.objects.filter(beach__name=beachName)[:commentAmount], #front-end needs button that modifies the commentAmount variable
        'beach': Beach.objects.filter(name=beachName).first,
        'request' : request
        #'comments': Comment.objects.all()[:69],
    }
    return render(request, 'beach/display.html', context)

def average(request, beachName):
    currentBeach = Beach.objects.get(name=beachName)
    swimR=diveR=surfR=loungeR=boatR=isCleanR=safetyR = 0
    ratings = Rating.objects.filter(beach__name=beachName)
    count = ratings.count()
    if count == 0:
        return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")
    for rating in ratings:
        swimR += rating.swim
        diveR += rating.dive
        surfR += rating.surf
        loungeR += rating.lounge
        boatR += rating.boat
        isCleanR += rating.isClean
        safetyR += rating.safety
    
    currentBeach.swimRating = swimR/count
    currentBeach.diveRating = diveR/count
    currentBeach.surfRating = surfR/count
    currentBeach.loungeRating = loungeR/count
    currentBeach.boatRating = boatR/count
    currentBeach.isCleanRating = isCleanR/count
    currentBeach.safetyRating = safetyR/count
    currentBeach.overallRating = ((swimR/count)+(diveR/count)+(surfR/count)+(loungeR/count)+(boatR/count)+(isCleanR/count)+(safetyR/count))/7
    currentBeach.save()
    return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")

