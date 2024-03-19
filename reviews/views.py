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

def handling_404(rquest, exception):
    return render(request, '404.html')

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
    
    search_result = request.GET.get('searchform')
       
    search_results = GameReview.objects.filter(approved=True).order_by('-rating')
    
    if search_result:
        search_results = search_results.filter(
            Q(title__icontains=search_result) |
            Q(genre__name__icontains=search_result) |
            Q(tags__name__icontains=search_result) |
            Q(platforms__name__icontains=search_result)
        ).distinct()
        
    
    
    context = {
        'search_results': search_results,
        
    }
    
    return render(request, template, context)     
    
    

    

    



def review_detail(request, review_id):
    """
    The purpose of this view is to display the full details of
    a particular review. 
    """
    review = get_object_or_404(GameReview, pk=review_id)
    

    context = {
        'review': review,
        
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
    This view will display all unapproved reviews by the current
    user on the 'unapproved_reviews.html' template. With the use of a
    filter, only the current user's unapproved reviews will be displayed
    here.
    """
    unapproved_reviews = GameReview.objects.filter(author=request.user, approved=False)

    context = {
        'unapproved_reviews': unapproved_reviews
    }

    return render(request, 'reviews/unapproved_reviews.html', context)




def pending_reviews(request):
    """
    For superusers only.
    Superusers can see which reviews need to be approved by displaying
    unapproved reviews. If a user attempts to navigate to this page
    and is not a superuser, they will be directed to a template,
    `unauthorised.html`.
    """
    if not request.user.is_superuser:
        return render(request, 'unauthorised.html')

    pending_reviews = GameReview.objects.filter(approved=False)

    context = {
        'pending_reviews': pending_reviews,
    }

    return render(request, 'reviews/pending_reviews.html', context)


@login_required
def review_approval(request, pending_review_id):
    """
    For superusers only.
    From the review approval list, a superuser can approve
    or reject an review depending on the action of the button
    which is clicked. The `approve` action button will approve
    of an review. Similarly, the `reject` action button will
    reject the review and delete it from the database permanently.
    """
    if not request.user.is_superuser:
        return render(request, 'unauthorized.html')

    pending_review = get_object_or_404(GameReview, pk=pending_review_id)

    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'approve':
            pending_review.approved = True
            pending_review.save()
            messages.success(request, f'Review {pending_review.title} has been approved.')  # noqa

        elif action == 'reject':
            pending_review.delete()
            messages.success(request, 'Review has been rejected and deleted.')

        return redirect('pending-reviews')

    # If the request method is not POST, render the approval form
    context = {
        'pending_review': pending_review,
    }

    return render(request, 'reviews/review_approval.html', context)

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
def edit_review(request, review_id):
    review = get_object_or_404(GameReview, pk=review_id)
    if review.author != request.user:
        messages.error(request, 'Access denied. Please make sure this is a review you created.')
        return redirect('home')
    # user matches the review author / proceed
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
def delete_review(request, review_id):
    """
   A logged in user has the ability to delete their own
    review. A superuser has the ability to delete any review,
    enabling them to keep the site clean of redundant reviews.

    Should a user attempt to perform this functionality and they
    aren't a superuser/the user who created the review, they will
    receive an error message.
    """
    review = get_object_or_404(GameReview, pk=review_id)

    if request.user == review.author or request.user.is_superuser:
        review.delete()
        messages.success(request, f"{review.title} successfully deleted.")

    else:
        messages.error(request, "You don't have permission to delete that review.")  

    return redirect('home')
   
   
   
   
   
   
   
   
