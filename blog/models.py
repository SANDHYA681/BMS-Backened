from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    author = models.CharField(max_length=50, default='Anonymous')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)  # ✅ For Featured Blogs section

    def __str__(self):
        return f"{self.title} by {self.author}"
