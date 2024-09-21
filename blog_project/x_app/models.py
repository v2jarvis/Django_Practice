# import necessary modules
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    Model for blog posts
    """

    title = models.CharField(
        max_length=128,
    )
    body = models.TextField()
    headline = models.TextField()
    image = models.ImageField(default="default.jpg", upload_to="Posts-Images")
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", null=True, blank=True
    )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """
        Returns the url to access a particular post instance.
        """
        return reverse("detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    """
    Model for comments
    """

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)                                                                                                                                                                                                                                                                                                                                                                                                                
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Like(models.Model):
    """
    Model for likes
    """

    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")


class Dislike(models.Model):
    """
    Model for dislikes
    """

    post = models.ForeignKey(Post, related_name="dislikes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
