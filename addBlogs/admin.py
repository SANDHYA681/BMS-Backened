from django.contrib import admin
from addBlogs import models

class addBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'updated_at')  # added 'status'
    search_fields = ['title', 'author__username', 'content']  # extended for better search
    list_filter = ('status', 'created_at', 'category')  # optional filters
    date_hierarchy = 'created_at'  # optional for time navigation

admin.site.register(models.addBlog, addBlogAdmin)
admin.site.register(models.Category)
