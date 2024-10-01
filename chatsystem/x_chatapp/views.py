"""
This is view file and on the upper import necessary modules
"""

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View

from .models import *


class IndexView(View):
    """
    This is the main view of the application.
    """

    def get(self, request):
        """
        This function renders the index page and excludes the logged-in user's details.
        """
        current_user = request.user
        users = User.objects.exclude(id=current_user.id)
        return render(request, "index.html", {"users": users})


@method_decorator(login_required, name="dispatch")
class UnreadMessageCountView(View):
    """
    This view returns the count of unread messages for each user.
    """

    def get(self, request):
        unread_counts = {}
        users = User.objects.exclude(id=request.user.id)
        for user in users:
            unread_count = Message.objects.filter(
                sender=user, recipient=request.user, is_read=False
            ).count()
            unread_counts[user.id] = unread_count

        return JsonResponse({"unread_counts": unread_counts})


@method_decorator(login_required, name="dispatch")
class SendMessageView(View):
    """
    This view handles sending messages between users.
    """

    def post(self, request):
        """
        This function creates a new message and saves it to the database.
        """
        recipient_id = request.POST.get("recipient")
        message_text = request.POST.get("message")
        recipient = User.objects.get(id=recipient_id)
        message = Message.objects.create(
            sender=request.user, recipient=recipient, text=message_text
        )
        formatted_time = message.timestamp.strftime("%I:%M %p")
        return JsonResponse(
            {
                "message": message.text,
                "sender": request.user.username,
                "timestamp": formatted_time,
            }
        )


class FetchMessagesView(View):
    """
    This is the view for fetching messages.
    """

    def post(self, request):
        """
        This is the post method for fetching messages.
        """
        user_id = request.POST.get("user_id")
        Message.objects.filter(
            sender=user_id, recipient=request.user, is_read=False
        ).update(is_read=True)

        messages = Message.objects.filter(
            (models.Q(sender=request.user) & models.Q(recipient_id=user_id))
            | (models.Q(sender_id=user_id) & models.Q(recipient=request.user))
        ).order_by("timestamp")

        message_list = []
        for msg in messages:
            local_time = timezone.localtime(msg.timestamp).strftime("%I:%M %p")
            message_list.append(
                {
                    "sender": msg.sender.username,
                    "text": msg.text,
                    "timestamp": local_time,
                }
            )

        return JsonResponse({"messages": message_list})


def register(request):
    """
    View function to register a user using Django's default User model.
    """
    if request.method == "POST":
        first = request.POST.get("first_name", "").strip()
        last = request.POST.get("last_name", "").strip()
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        cpass = request.POST.get("password", "").strip()
        rpass = request.POST.get("repeat_password", "").strip()
        super_user = request.POST.get("super", "False") == "1"
        staff = request.POST.get("staff", "False") == "1"

        if cpass == rpass:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect("/register/")
            user = User(
                first_name=first,
                last_name=last,
                username=username,
                email=email,
                is_superuser=super_user,
                is_staff=staff,
                is_active=True,
            )
            user.set_password(cpass)
            user.save()
            return redirect("/")
        else:
            messages.error(request, "Passwords do not match.")
            return redirect("/")
    return redirect("/")


def user_login(request):
    """
    Login function that authenticates the user and manages session.
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("/login/")
    return redirect("/")


def user_logout(request):
    """
    Logout function that removes the user session.
    """
    logout(request)
    request.session.clear()
    return redirect("/")

