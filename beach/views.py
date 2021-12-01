from os import name
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Comment, Beach, Rating
from .forms import CommentForm, RatingForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Can map URL's to views.
commentAmount = 3

def display(request, beachName='Jobos'):
    
    beach = Beach.objects.filter(name=beachName).first
    prevRating = Rating.objects.filter(author__username = request.user.username).filter(beach__name = beachName)
    if request.method == 'POST':
        ratingForm = RatingForm(request.POST)
        commentForm = CommentForm(request.POST)
        if ratingForm.is_valid() and commentForm.is_valid() and prevRating.count() == 0:
            ratingForm.save()
            commentForm.save()
            average(request, beachName)
            messages.success(request, f'Your review was submitted!')
        else:
            messages.error(request, f'Something went wrong, your review was not sent')
        return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")

    else: #get request
        ratingForm = RatingForm(initial = {'beach' : beach, 'author':  request.user})
        commentForm = CommentForm(initial = {'beach' : beach, 'author':  request.user})
        ratingForm.fields['beach'].widget = forms.HiddenInput()
        ratingForm.fields['author'].widget = forms.HiddenInput()
        commentForm.fields['beach'].widget = forms.HiddenInput()
        commentForm.fields['author'].widget = forms.HiddenInput()

        #Key -> Username, Value -> Rating
        userRatings = {}
        for rating in Rating.objects.filter(beach__name = beachName):
            userRatings[rating.author.username] = rating.overall
        context = {
            'comments': Comment.objects.filter(beach__name=beachName)[:commentAmount], #front-end needs button that modifies the commentAmount variable
            'beach': beach,
            'ratingForm': ratingForm,
            'commentForm' : commentForm,
            'userRatings' : userRatings,
            'request' : request
        #'comments': Comment.objects.all()[:69],
        }
        return render(request, 'beach/display.html', context)

@login_required
def addReview(request, beachName):
    
    return render(request, 'beach/' + beachName, {})

def average(request, beachName):
    #dont touch this, please
    currentBeach = Beach.objects.get(name=beachName)
    overallR=swimR=diveR=surfR=loungeR=boatR=isCleanR=safetyR = 0
    ratingCount = {'swim': 0, 'dive' : 0, 'surf': 0, 'lounge' :0, 'boat' : 0, 'isClean' : 0, 'safety': 0}
    ratings = Rating.objects.filter(beach__name=beachName)
    count = ratings.count()
    if count == 0:
        return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")
    for rating in ratings:
        if rating.swim is not None:
            swimR += rating.swim
            ratingCount['swim'] += 1

        if rating.dive is not None:
            diveR += rating.dive
            ratingCount['dive'] += 1

        if rating.surf is not None:
            surfR += rating.surf
            ratingCount['surf'] += 1

        if rating.lounge is not None:
            loungeR += rating.lounge
            ratingCount['lounge'] += 1

        if rating.boat is not None:
            boatR += rating.boat
            ratingCount['boat'] += 1

        if rating.isClean is not None:
            isCleanR += rating.isClean
            ratingCount['isClean'] += 1

        if rating.safety is not None:
            safetyR += rating.safety
            ratingCount['safety'] += 1

        overallR += rating.overall
        
    #if 0 count, set to 1 so that it wont break division, result will still be 0
    for k, v in ratingCount.items():
        if v == 0:
            ratingCount[k] = 1

    #reuse dictionary, now store the average rating in them
    ratingCount['swim'] = swimR / ratingCount['swim']
    ratingCount['dive'] = diveR/ratingCount['dive']
    ratingCount['surf'] = surfR/ratingCount['surf']
    ratingCount['lounge']= loungeR/ratingCount['lounge']
    ratingCount['boat'] = boatR/ratingCount['boat']
    ratingCount['isClean'] = isCleanR/ratingCount['isClean']
    ratingCount['safety'] = safetyR/ratingCount['safety']
    ratingCount['overall'] = overallR/count
    #if a rating is 0, ignore it in overall Rating
    add = 0.0
    div = 1
    for k, v in ratingCount.items():
        if v != 0:
            if k == 'swim':
                add += ratingCount['swim']
                currentBeach.swimRating = ratingCount['swim']
                div+=1
            if k == 'lounge':
                add += ratingCount['lounge']
                currentBeach.loungeRating = ratingCount['lounge']
                div+=1
            if k == 'dive':
                add += ratingCount['dive']
                currentBeach.diveRating = ratingCount['dive']
                div+=1
            if k == 'surf':
                add += ratingCount['surf']
                currentBeach.surfRating = ratingCount['surf']
                div+=1
            if k == 'boat':
                add += ratingCount['boat']
                currentBeach.boatRating = ratingCount['boat']
                div+=1
            if k == 'isClean':
                add += ratingCount['isClean']
                currentBeach.isCleanRating = ratingCount['isClean']
                div+=1
            if k == 'safety':
                add += ratingCount['safety']
                currentBeach.safetyRating = ratingCount['safety']
                div+=1
    
    add += ratingCount['overall']
    currentBeach.overallRating = add/div
    currentBeach.save()
    return HttpResponse("""<html><script>window.location.replace('/beach/""" + beachName + """/');</script></html>""")


