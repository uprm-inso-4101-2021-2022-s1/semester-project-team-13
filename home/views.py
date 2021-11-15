from django.shortcuts import render
from django.utils.datastructures import OrderedSet
from beach.models import Comment, Beach, Rating
from django.http import HttpResponse
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

topOverallRatings = Rating.objects.order_by('-overall')

def home(request):

    beachesCommentAmount = {}
    
    for rating in topOverallRatings:
        # Key -> Beach name (str), Value = comment amount (int)
        beachesCommentAmount[str(rating.beach.name)] = Comment.objects.filter(beach__name=rating.beach.name).count()

    context = {
        #sort by overall beach rating
        'topOverallRatings' : topOverallRatings,
        'beachesCommentAmount' : beachesCommentAmount,
    }
    return render(request, 'home/home.html', context)

def reverseList(request):
    global topOverallRatings
    topOverallRatings = Rating.objects.order_by('overall')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def undoReverse(request):
    global topOverallRatings
    topOverallRatings = Rating.objects.order_by('-overall')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def sortBy(request, type):
    global topOverallRatings
    topOverallRatings = Rating.objects.order_by('-' + type)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def sortByRegion(request, region):
    global topOverallRatings
    topOverallRatings = Rating.objects.filter(beach__region=region)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def showAllRegions(request):
    global topOverallRatings
    topOverallRatings = Rating.objects.order_by('-overall')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    
