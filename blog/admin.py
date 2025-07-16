from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'featured', 'created_at')  # ✅ removed 'top'
    list_filter = ('featured', 'created_at')                      # ✅ removed 'top'
    search_fields = ('title', 'author')  # ✅ admin search box

admin.site.register(Blog, BlogAdmin)
