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


# Index/Home page
def index(request):
    """
    This simple view will render the index.html template
    which is the homepage of the site.
    """
    return render(request, 'reviews/index.html')


# About page
def about(request):
    """
    This simple view will render the about.html template
    which is the about page of the site.
    """
    return render(request, 'reviews/about.html')


# Profile page
def profile(request):
    """
    This simple view will render the profile.html template
    which is the profile of the site.
    """
    return render(request, 'reviews/profile.html')


# Render all reviews
class AllReviews(generic.ListView):
    """
    This simple view will render all approved reviews to the all_reviews.html page
    """
    queryset = GameReview.objects.filter(approved=True)
    template_name = "reviews/all_reviews.html"
    paginate_by = 6


# Search reviews
def search_reviews(request):
    """
    This view will get the value of the `searchform`
    and pass it into the variable `search_result`,
    All approved reviews will then be passed into the variable
    `search_results` and ordered by rating.
    This variable will then be checked and filtered by a list of search
    queries which checks which objects titles,genre,tags or platforms
     in search_results contain the value of `search_result` i.e what
     the user typed into the search bar, ensuring only reviews that contain the
     searched query are rendered to the user.
    """
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


# Review detail, extended information and full review
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


# User's approved reviews, requires login
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


# User's unapproved reviews, requires login
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


# Reviews that are pending approval from an admin, superusers only
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


# Approval of pending reviews, super users only
@login_required
def review_approval(request, pending_review_id):
    """
    For superusers only.
    From the review approval list, a superuser can approve
    a review, this will update the approved field to True, moving the
    review into the approved section on the DB and it will subsequently be
    rendred on the all_reviews.html page and the users approved reviews page

    """
    if not request.user.is_superuser:
        return render(request, 'unauthorized.html')

    pending_review = get_object_or_404(GameReview, pk=pending_review_id)

    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'approve':
            pending_review.approved = True
            pending_review.save()
            messages.success(request, f'Review {pending_review.title} has been approved.')

        return redirect('pending-reviews')

    context = {
        'pending_review': pending_review,
    }

    return render(request, 'reviews/review_approval.html', context)


# Create Review using ReviewForm
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
            messages.success(request, "Your review has been submitted and is pending approval by an admin.")

            return redirect('home')
    else:
        form = ReviewForm()

    context = {
        'form': form,
    }

    return render(request, 'reviews/create_review.html', context)


# Edit review using ReviewForm
@login_required
def edit_review(request, review_id):
    """
    An edit button will be available on the review_detail page if they
    are the author of that review.
    Using the `ReviewForm`, users can edit this review
    The fields will be prepopulated with the
    exact same data as the current review by creating an
    instance of the current review and rendering that
    as a new form to be edited. Once the changes are submitted,
    the edited review will go back up for approval by an admin.
    """
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


# Delete review
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
