from django import forms
from .models import Rating, Beach
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        swim = forms.MultipleChoiceField(required=False)
        dive = forms.MultipleChoiceField(required=False)
        surf = forms.MultipleChoiceField(required=False)
        lounge = forms.MultipleChoiceField(required=False)
        boat = forms.MultipleChoiceField(required=False)
        isClean = forms.MultipleChoiceField(required=False) 
        safety = forms.MultipleChoiceField(required=False) 

        labels = {
        "overall" : "Your overall experience",
        "swim": "Swimming",
        "dive": "Diving",
        "surf" : "Surfing",
        "lounge" : "Lounging",
        "boat" : "Boating",
        "isClean": "Cleanliness",
        "safety" : "Safe"
        }
        
        fields = ['overall', 'swim', 'dive', 'surf', 'lounge', 'boat', 'isClean', 'safety', 'beach', 'author']

        #comment = forms.CharField(widget=forms.Textarea)
#class CommentForm(forms.ModelForm)
