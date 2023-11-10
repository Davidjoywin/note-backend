from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, auto_created=True, blank=True)
    title = models.CharField(max_length=60, blank=True)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return f"{self.user.username} -> {self.title}"
        return self.title