from os import name
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Comment, Beach, Rating
from .forms import RatingForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Can map URL's to views.
commentAmount = 3

def display(request, beachName='Jobos'):
    
    beach = Beach.objects.filter(name=beachName).first

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")

    else: #get request
        form = RatingForm(initial = {'beach' : beach, 'author':  request.user})
        form.fields['beach'].widget = forms.HiddenInput()
        form.fields['author'].widget = forms.HiddenInput()

        context = {
            'comments': Comment.objects.filter(beach__name=beachName)[:commentAmount], #front-end needs button that modifies the commentAmount variable
            'beach': beach,
            'form': form,
            'request' : request
        #'comments': Comment.objects.all()[:69],
        }
        return render(request, 'beach/display.html', context)

@login_required
def addReview(request, beachName):
    
    return render(request, 'beach/' + beachName, {})

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


