from django.db.models.query import QuerySet
from django.shortcuts import render
from beach.models import Comment, Beach, Profile, Rating
from users.views import profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def userProfile(request, username='jeremy'): #if profile ID doesn't exist we must redirect to the login page.
    #when implementing via the admin page, create a profile in the process
    bListString = Profile.objects.get(user__username=username).bucketList
    #crashboat,jobos,
    bList = bListString.rsplit(",")

    recentComments = {}
    ratings = Rating.objects.filter(author__username=username).order_by('date_posted')[:5]
    comments = Comment.objects.filter(author__username=username).order_by('date_posted')[:5]
    i=0
    for comment in comments:
        recentComments[ratings[i].id] = comment.content
        i += 1

    context = {
        #sort by overall beach rating
        'profile': Profile.objects.filter(user__username=username)[0],
        'bucketList': Beach.objects.filter(name__in=bList),
        'recentRatings': ratings,
        'recentComments': recentComments
    }
    return render(request, 'userProfile/userProfile.html', context)

@login_required
def add(request, beachName):
    currentUser = request.user
    userProfile = Profile.objects.get(user__username=currentUser.username)
    if(userProfile.bucketList.rfind(beachName) == -1):
        userProfile.bucketList += beachName + ","
        userProfile.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
@login_required
def remove(request, username, beachName):
    userProfile = Profile.objects.get(user__username=username)
    if(userProfile.bucketList.rfind(beachName) != -1 and request.user.username == username):
        toRemove = beachName+","
        userProfile.bucketList = userProfile.bucketList.replace(toRemove, "")
        userProfile.save()
    return HttpResponse("""<html><script>window.location.replace('/profile/""" + username + """/');</script></html>""")
