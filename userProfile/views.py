from django.shortcuts import render
from beach.models import Comment, Beach, Profile
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def userProfile(request, username='jeremy'): #if profile ID doesn't exist we must redirect to the login page.
    #when implementing via the admin page, create a profile in the process
    context = {
        #sort by overall beach rating
        'profile': Profile.objects.filter(user__username=username)[0],
        
    }
    return render(request, 'userProfile/userProfile.html', context)
