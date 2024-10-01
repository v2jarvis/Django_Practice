"""
This is models file on the top import necessary modules
"""

from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    """
    This is Message model
    """

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender.username} to {self.recipient.username}: {self.text}"
