from django.shortcuts import render
from .models import Comment
# Views are like request handlers.
# Can map URL's to views.
# Create your views here.

def home(request):
    context = {
        'comments': Comment.objects.all(),
        
    }
    return render(request, 'beach/display.html', context)