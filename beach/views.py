from django.shortcuts import render
from .models import Comment
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def display(request, beachName='jobos'):
    context = {
        'comments': Comment.objects.filter(beach__name=beachName),
        #'comments': getComment(),
    }
    return render(request, 'beach/display.html', context)
