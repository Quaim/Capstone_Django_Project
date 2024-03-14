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

class AllReviews(generic.ListView):
    queryset = GameReview.objects.filter(approved=True)
    template_name = "reviews/all_reviews.html"
    paginate_by = 6