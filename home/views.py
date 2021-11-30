from django.shortcuts import render
from django.utils.datastructures import OrderedSet
from beach.models import Comment, Beach, Rating
from django.http import HttpResponse
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

topOverallBeaches = Beach.objects.order_by('-overallRating')

def home(request):

    beachesCommentAmount = {}
    
    for beach in topOverallBeaches:
        # Key -> Beach name (str), Value = comment amount (int)
        beachesCommentAmount[str(beach.name)] = Comment.objects.filter(beach__name=beach.name).count()

    context = {
        #sort by overall beach rating
        'topOverallBeaches' : topOverallBeaches,
        'beachesCommentAmount' : beachesCommentAmount,
    }
    return render(request, 'home/home.html', context)

def reverseList(request):
    global topOverallBeaches
    topOverallBeaches = Beach.objects.order_by('overallRating')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def undoReverse(request):
    global topOverallBeaches
    topOverallBeaches = Beach.objects.order_by('-overallRating')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def sortBy(request, type):
    global topOverallBeaches
    topOverallBeaches = Beach.objects.order_by('-' + type)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def sortByRegion(request, region):
    global topOverallBeaches
    topOverallBeaches = Beach.objects.filter(region=region)
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def showAllRegions(request):
    global topOverallBeaches
    topOverallBeaches = Beach.objects.order_by('-overallRating')
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")
    
