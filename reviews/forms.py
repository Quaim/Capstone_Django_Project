from django import forms
from django.forms import CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple
from .models import GameReview, Tag, Platform





class CreateReview(forms.ModelForm):
    """
    Form for users to create events which works off the `EventModel`.
    Uses widgets to assign input types to `event_date` and `event_time`.
    Also assigns classes to input fields.
    """
    class Meta:
        model = GameReview
        fields = [
            'title',
            'description',
            'genre',
            'tags',
            'platforms',
            'review',
            'rating',
            'featured_image',         
            
            
        ]
        # # tags = forms.ModelMultipleChoiceField(
        
        # #     label="Tags",
        # #     queryset = Tag.objects.all(),
        # #     widget=forms.CheckboxSelectMultiple(attrs={
        # #     'class': 'form-check-input',
        # # }),
        
        # )