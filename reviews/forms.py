from django import forms
from .models import GameReview, Tag, Platform


# Form for creating or editing reviews
class ReviewForm(forms.ModelForm):
    """
    A form to allow users to create a game review.

    create a variable for platform and tags to be used on
    the form, this is required as manytomanyfields are not
    automatically usable in django forms by default,
    also sets the widget to a checkbox for each tag/platform
    in the model so users can select multiple ones to then
    be used in the relevant views
    """
    platforms = forms.ModelMultipleChoiceField(
        queryset=Platform.objects.all().order_by("name"),
        help_text = "Select multiple if needed",
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input",
            }
        ),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by("name"),
        help_text = "Select multiple if needed",
        widget=forms.CheckboxSelectMultiple(
            attrs={
                "class": "form-check-input",
            }
        ),
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