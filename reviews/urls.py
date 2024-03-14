from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('all-reviews/', views.AllReviews.as_view(), name='all-reviews'),
    path('review/<int:gamereview_id>/', views.review_detail, name='review_detail'),

]