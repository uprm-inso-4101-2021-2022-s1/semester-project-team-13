from django.db.models.query import QuerySet
from django.shortcuts import render
from beach.models import Comment, Beach, Profile, Rating
from users.views import profile
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def userProfile(request, username='jeremy'): #if profile ID doesn't exist we must redirect to the login page.
    #when implementing via the admin page, create a profile in the process
    bListString = Profile.objects.get(user__username=username).bucketList
    #crashboat,jobos,
    bList = bListString.rsplit(",")

    context = {
        #sort by overall beach rating
        'profile': Profile.objects.filter(user__username=username)[0],
        'bucketList': Rating.objects.filter(beach__name__in=bList)
    }
    return render(request, 'userProfile/userProfile.html', context)
