from django import forms
from .models import Comment, Rating, Beach

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

       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        content = forms.CharField(widget=forms.Textarea)
        labels = {
            "content" : 'Write your experience!'
        }
        fields = ['content', 'beach', 'author']