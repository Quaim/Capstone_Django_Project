from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('all-reviews/', views.AllReviews.as_view(), name='all-reviews'),
    path('review/<int:gamereview_id>/', views.review_detail, name='review-detail'),
    path('create-review/', views.create_review, name='create-review'),
    path('edit-review/<int:gamereview_id>/', views.edit_review, name='edit-review'),
    path('delete-review/<int:gamereview_id>/', views.delete_review, name='delete-review'),
    path('approved-reviews/', views.user_approved_reviews, name='approved-reviews'),
    path('unapproved-reviews/', views.user_unapproved_reviews, name='unapproved-reviews'),
    path('search-result/', views.search_reviews, name='search-results')

]