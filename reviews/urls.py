from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all-reviews/', views.AllReviews.as_view(), name='all-reviews'),

]