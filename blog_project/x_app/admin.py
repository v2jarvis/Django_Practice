# import necessary moduls
from django.contrib import admin

from x_app.models import Comment, Dislike, Like, Post


class BlogAdmin(admin.ModelAdmin):
    """
    BlogAdmin is a custom admin interface for the Blog model.
    """

    list_display = ["title", "body", "headline", "image"]
    prepopulated_fields = {"slug": ("title",)}


# register your models
admin.site.register(Post, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)  # Register the Dislike model
