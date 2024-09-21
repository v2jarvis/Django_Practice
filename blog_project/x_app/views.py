"""
this is my views.py file for my blog app and on the top,
I import the needed modules and then one by one all over
the functions
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Dislike, Like, Post


def blog_post(request):
    """
    This function is used to post a blog.
    """
    if request.method == "POST":
        title = request.POST.get("title", "")
        body = request.POST.get("body", "")
        headline = request.POST.get("headline", "")
        image = request.FILES.get("image", "")
        slug = request.POST.get("slug", "")
        user = request.user
        post = Post(title=title, body=body, headline=headline, image=image, slug=slug, user=user)
        post.save()

        return redirect("/")
    return render(request, "blog_post.html")

def index(request):
    """
    View function for the index page.
    """
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def detail(request, slug):
    """
    View function for the post detail page.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "detail.html", {"post": post})

def edit_blog(request, slug):
    """
    edit function that perform to open the database data which are hit by edit button
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_edit.html", {"data": post})

def update(request, slug):
    """
    Update function to perform the update of data like partially or fully.
    """
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        title = request.POST.get("title", post.title)
        body = request.POST.get("body", post.body)
        headline = request.POST.get("headline", post.headline)
        image = request.FILES.get("image", post.image)
        new_slug = request.POST.get("slug", post.slug)

        post.title = title
        post.body = body
        post.headline = headline
        post.image = image
        post.slug = new_slug
        post.save()
        return redirect("detail", slug=post.slug)
    return redirect("editblog", slug=slug)

def register(request):
    """
    View function to register a user using Django's default User model.
    """
    if request.method == "POST":
        first = request.POST.get("first", "").strip()
        last = request.POST.get("last", "").strip()
        username = request.POST.get("user", "").strip()
        email = request.POST.get("email", "").strip()
        cpass = request.POST.get("cpass", "").strip()
        rpass = request.POST.get("rpass", "").strip()
        super_user = request.POST.get("super", "True")
        staff = request.POST.get("staff", "True")

        if cpass == rpass:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect("register")
            user = User(
                first_name=first,
                last_name=last,
                username=username,
                email=email,
                is_superuser=super_user,
                is_staff=staff,
                is_active=True,
            )
            user.set_password(rpass)
            user.save()
            messages.success(request, "Successfully Registered.")
            return redirect("/")
        else:
            messages.error(request, "Passwords do not match.")
            return redirect("/")
    else:
        return redirect("/")

def user_login(request):
    """
    Login function that authenticates the user and manages session.
    """
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Login.")
            request.session["username"] = user.username
            return redirect("/")
        else:
            return HttpResponse("<script>alert('Password Not Match');</script>")
    return redirect("/")

def user_logout(request):
    """
    Logout function that removes the user session.
    """
    logout(request)
    request.session.clear()
    messages.success(request, "Successfully Logout.")
    return redirect("/")

def search_posts(request):
    """
    Function to search posts.
    """
    query = request.GET.get("q", "")
    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    return render(request, "index.html", {"posts": posts})

def del_blog(request, slug):
    """
    Function to delete posts.
    """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect("/")

def add_comment(request, slug):
    """
    Function to add comment to a post.
    """
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        body = request.POST.get("body")
        if request.user.is_authenticated:
            comment = Comment(post=post, author=request.user, body=body)
            comment.save()
    return redirect("detail", slug=post.slug)

def like_post(request, slug):
    """
    Function to like a post.
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        Like.objects.get_or_create(post=post, user=request.user)
    return redirect("detail", slug=post.slug)

def dislike_post(request, slug):
    """
    Function to dislike a post.
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_authenticated:
        Dislike.objects.get_or_create(post=post, user=request.user)
    return redirect("detail", slug=post.slug)
