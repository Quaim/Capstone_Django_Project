from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Simple model for Genre's to be added to the GameReview model
class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# Simple model for Tag's to be addded to the GameReview model
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# Simple model for Platforms's to be addded to the GameReview model
class Platform(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# Main GameReview model to be used in form and views to generate
# reviews on the frontend and backend
class GameReview(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='game_reviews', null=True
        )
    title = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=200, blank=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, null=True, blank=False
        )
    tags = models.ManyToManyField('Tag')
    platforms = models.ManyToManyField('Platform')
    description = models.CharField(max_length=250, null=False, blank=False)
    featured_image = CloudinaryField("image", default="placeholder")
    review = models.TextField(null=False, blank=False)
    rating = models.PositiveIntegerField(
        default=1, choices=[(i, i) for i in range(1, 6)]
        )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
