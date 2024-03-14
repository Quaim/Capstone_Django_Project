from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

from .models import GameReview

def index(request):
    return render(request, 'reviews/index.html')

def about(request):
    return render(request, 'reviews/about.html')

class AllReviews(generic.ListView):
    queryset = GameReview.objects.filter(approved=True)
    template_name = "reviews/all_reviews.html"
    paginate_by = 6

def review_detail(request, gamereview_id):
    """
    The purpose of this view is to display the full details of
    a particular event. Reviews for the selected event will
    also be shown at the bottom of the current event details.
    Providing the currently logged in user isn't the user who
    created the event, they can also submit a new review which
    will be put up for approval by an admin.
    """
    gamereview = get_object_or_404(GameReview, pk=gamereview_id)
    

    context = {
        'gamereview': gamereview,
        
    }

    return render(request, 'reviews/review_detail.html', context)