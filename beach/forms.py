from django import forms
from .models import Rating, Beach
from django.contrib.auth.models import User

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        swim = forms.IntegerField(required=False)
        dive = forms.IntegerField(required=False)
        surf = forms.IntegerField(required=False)
        lounge = forms.IntegerField(required=False)
        boat = forms.IntegerField(required=False)
        isClean = forms.IntegerField(required=False) 
        safety = forms.IntegerField(required=False) 
        fields = ['overall', 'swim', 'dive', 'surf', 'lounge', 'boat', 'isClean', 'beach', 'author']
