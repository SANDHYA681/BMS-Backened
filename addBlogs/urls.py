from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Static Pages
    path('about/', views.about_us, name='about_us'),

    # Advanced Blog (addBlog) Routes
    path('blogs/', views.blog, name='blogs'),  # All blogs
    path('blogs/add/', views.addBlogs, name='add_blog'),  # Add new blog
    path('blogs/edit/<int:id>/', views.editBlogPage, name='edit_blog_page'),  # Edit form
    path('blogs/update/<int:id>/', views.editBlog, name='edit_blog'),  # Save update
    path('blogs/<int:blog_id>/', views.blogDetails, name='blog_details'),  # Blog details
    path('blogs/type/<str:type>/', views.blogs_by_type, name='blogs_by_type'),  # Blogs by category
    path('my-blogs/', views.my_blogs, name='my_blogs'),  # My Blogs (User-specific)

    # Optional: Old Blog model routes
    path('blogs/simple/add/', views.addSimpleBlog, name='add_simple_blog'),
    path('blogs/simple/', views.simpleBlogList, name='simple_blog_list'),
]
