from django.shortcuts import render
from beach.models import Comment, Beach, Rating
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def home(request):

    beachesCommentAmount = {}
    topOverallRatings = Rating.objects.order_by('-overall')
    for rating in topOverallRatings:
        # Key -> Beach name (str), Value = comment amount (int)
        beachesCommentAmount[str(rating.beach.name)] = Comment.objects.filter(beach__name=rating.beach.name).count()

    context = {
        #sort by overall beach rating
        'topOverallRatings' : topOverallRatings,
        'beachesCommentAmount' : beachesCommentAmount
    }
    return render(request, 'home/home.html', context)
