from django.contrib import admin
from .models import GameReview, Genre, Tag, Platform
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(GameReview)
class GameReviewAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slug', 'approved', 'created_on')
    search_fields = ['title', 'review']
    list_filter = ('approved','created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('review',)


admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Platform)
