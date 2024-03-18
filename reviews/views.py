from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.urls import reverse

from .models import GameReview
from .forms import ReviewForm

def index(request):
    return render(request, 'reviews/index.html')


def about(request):
    return render(request, 'reviews/about.html')

def profile(request):
    return render(request, 'reviews/profile.html')

class AllReviews(generic.ListView):
    queryset = GameReview.objects.filter(approved=True)
    template_name = "reviews/all_reviews.html"
    paginate_by = 6


def search_reviews(request):
    template = 'reviews/search_result.html'

    if request.method == 'POST':
        search_result = request.POST['searchform']

        search_results = GameReview.objects.filter(Q(title__icontains=search_result) | Q(genre__name__icontains=search_result) | Q(tags__name__icontains=search_result)
         | Q(platforms__name__icontains=search_result))
        context = {
        'search_results': search_results,
        
    }
        if not search_result:
             messages.success(request, "No Reviews containing your query exist, please check spelling just incase")
             return render(request, template)
        else:
            return render(request, template, context)     
    
    

    return render(request, template, context)

    



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
def user_approved_reviews(request):
    """
    This view will display all approved reviews by the current
    user on the 'approved_reviews.html' template. With the use of a
    filter, only the current user's approved reviews will be displayed
    here.
    """
    approved_reviews = GameReview.objects.filter(author=request.user, approved=True)

    context = {
        'approved_reviews': approved_reviews
    }

    return render(request, 'reviews/approved_reviews.html', context)

@login_required
def user_unapproved_reviews(request):
    """
    This view will display all approved reviews by the current
    user on the 'approved_reviews.html' template. With the use of a
    filter, only the current user's approved reviews will be displayed
    here.
    """
    unapproved_reviews = GameReview.objects.filter(author=request.user, approved=False)

    context = {
        'unapproved_reviews': unapproved_reviews
    }

    return render(request, 'reviews/unapproved_reviews.html', context)


# class UserApprovedReviews(generic.ListView):
#     queryset = GameReview.objects.filter(approved=True, author=request.user)
#     template_name = "reviews/user_approved_reviews.html"
#     paginate_by = 6






@login_required
def create_review(request):
    """
    Logged in users will be able to create a review using the `CreateReview` Form which uses fields from the
    `GameReviewModel`. Once a review has been created, it will
    be put up for review by an admin and redirect the user back
    to the home page.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            form.save_m2m()

            messages.success(request, "Your review has been submitted and is pending approval.")  

            return redirect('home')
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }

    return render(request, 'reviews/create_review.html', context)


@login_required
def edit_review(request, gamereview_id):
    review = get_object_or_404(GameReview, pk=gamereview_id)
    if review.author != request.user:
        messages.error(request, 'Access denied. Please make sure this is a review you created.')
        return redirect('home')
    # user matches the book user / proceed
    form = ReviewForm(request.POST or None, request.FILES, instance=review)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            review.approved = False
            form.save()
            

            messages.success(request, 'Review successfuly updated and is now up for approval by an admin')
            return redirect('home')
        messages.error(request, 'An error occurred. Please try again.')
    form = ReviewForm(instance=review)
    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review
    }
    return render(request, template, context)

@login_required
def delete_review(request, gamereview_id):
    """
   A logged in user has the ability to delete their own
    review. A superuser has the ability to delete any review,
    enabling them to keep the site clean of redundant events.

    Should a user attempt to perform this functionality and they
    aren't a superuser/the user who created the review, they will
    receive an error message.
    """
    review = get_object_or_404(GameReview, pk=gamereview_id)

    if request.user == review.author or request.user.is_superuser:
        review.delete()
        messages.success(request, f"{review.title} successfully deleted.")

    else:
        messages.error(request, "You don't have permission to delete that review.")  

    return redirect('home')
   
   
   
   
   
   
   
   
