from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

from .models import GameReview
from .forms import CreateReview, EditReview

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
    a particular review. 
    """
    gamereview = get_object_or_404(GameReview, pk=gamereview_id)
    

    context = {
        'gamereview': gamereview,
        
    }

    return render(request, 'reviews/review_detail.html', context)


@login_required
def create_review(request):
    """
    Logged in users will be able to create a review using the `CreateReview` Form which uses fields from the
    `GameReviewModel`. Once a review has been created, it will
    be put up for review by an admin and redirect the user back
    to the home page.
    """
    if request.method == 'POST':
        form = CreateReview(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            form.save_m2m()

            messages.success(request, "Your review has been submitted and is pending approval.")  

            return redirect('home')
    else:
        form = CreateReview()

    context = {
        'form': form,
    }

    return render(request, 'reviews/create_review.html', context)


@login_required
def edit_review(request, gamereview_id):
    review = get_object_or_404(GameReview, pk=gamereview_id, author=request.user)
    if review.author != request.user:
        messages.error(request, 'Access denied. Please try again.')
        return redirect('home')
    # user matches the book user / proceed
    form = EditReview(request.POST or None, request.FILES, instance=review)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            review.approved = False
            form.save()
            # form.save_m2m()

            messages.success(request, 'Review successfuly updated and it now up for approval by admin')
            return redirect('home')
        messages.error(request, 'An error occurred. Please try again.')
    form = EditReview(instance=review)
    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review
    }
    return render(request, template, context)
