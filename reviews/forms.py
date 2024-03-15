from django import forms

from .models import GameReview, Tag, Platform



class CreateReview(forms.ModelForm):
    """
    A form to allow users to create a game review.
    """
    platforms = forms.ModelMultipleChoiceField(
        queryset = Platform.objects.all().order_by("name"),
        widget = forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset = Tag.objects.all().order_by("name"),
        widget = forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )

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














# class CreateReview(forms.ModelForm):
#     """
    
#     """
#     class Meta:
#         model = GameReview
#         fields = [
#             'title',
#             'description',
#             'genre',
#             'tags',
#             'platforms',
#             'review',
#             'rating',
#             'featured_image',         
            
            
#         ]
#         tags = forms.ModelMultipleChoiceField(
        
#             label="Tags",
#             queryset = Tag.objects.all(),
#             widget=forms.CheckboxSelectMultiple(attrs={
#             'class': 'form-check-input',
#         }),
        
#         )