from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# -----------------------------
# Category Model
# -----------------------------
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# -----------------------------
# Full Blog Model (from before)
# -----------------------------
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    author = models.CharField(max_length=50, default='Anonymous')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    featured = models.BooleanField(default=False)  #  For Featured Blogs section

    def __str__(self):
        return f"{self.title} by {self.author}"


# -----------------------------
# New addBlog Model
# -----------------------------
class addBlog(models.Model):

    def generateImagePath(instance, filename):
        return f'blog/{instance.author.username}/images/{filename}'

    def generateAttachmentPath(instance, filename):
        return f'blog/{instance.author.username}/attachments/{filename}'

    class StatusOptions(models.TextChoices):
        ACTIVE = "Active", "Active"
        INACTIVE = "Rejected", "Rejected"
        PENDING = "Pending", "Pending"

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=generateImagePath, default='static/assets/blog1.png')
    attachment = models.FileField(blank=True, null=True, upload_to=generateAttachmentPath)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    tags = TaggableManager(blank=True)
    status = models.CharField(max_length=8, choices=StatusOptions.choices, default=StatusOptions.PENDING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    featured = models.BooleanField(default=False)  


    def __str__(self):
        return f"{self.title} by {self.author.username}"
