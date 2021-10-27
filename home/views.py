from django.shortcuts import render
from beach.models import Comment, Beach, Rating
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def home(request):
    context = {
        #sort by overall beach rating
        'topOverallRatings' : Rating.objects.order_by('-overall')
        
    }
    return render(request, 'home/home.html', context)
