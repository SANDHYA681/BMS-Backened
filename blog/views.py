# from django.shortcuts import render
# from blog.models import Blog
# from django.db.models import Q  # ✅ For searching by title

# # Home page view with optional search filtering
# def home(request):
#     query = request.GET.get('q')  # ✅ Get search query from input

#     # Featured blogs
#     featured_blogs = Blog.objects.filter(featured=True).order_by('-created_at')

#     # Recent blogs (non-featured)
#     recent_blogs = Blog.objects.exclude(id__in=featured_blogs.values_list('id', flat=True)).order_by('-created_at')

#     # ✅ Filter both sections if a search query is provided
#     if query:
#         featured_blogs = featured_blogs.filter(title__icontains=query)
#         recent_blogs = recent_blogs.filter(title__icontains=query)

#     return render(request, 'home.html', {
#         'featured_blogs': featured_blogs,
#         'recent_blogs': recent_blogs,
#     })

# # Category-based blog filtering
# def blogs_by_type(request, type):
#     blogs = Blog.objects.filter(type__iexact=type).order_by('-created_at')
#     return render(request, 'category_blogs.html', {
#         'blogs': blogs,
#         'category': type.capitalize()
#     })


from django.shortcuts import render
from blog.models import Blog
from django.contrib import messages
from django.db.models import Q

# ✅ Add Blog
def addBlogs(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')
        author = request.POST.get('author')

        blog = Blog(  # ✅ Corrected from models.Blog to Blog
            title=title,
            image=image,
            content=content,
            author=author
        )
        blog.save()
        messages.success(request, "Blog added successfully")  # ✅ Fixed

    return render(request, 'pages/blogs/add-blog.html')


# ✅ Blog list view (all blogs)
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'pages/blogs/blog.html', {'blogs': blogs})


# ✅ Home view with search for Top, Featured, and Recent blogs
def home(request):
    query = request.GET.get('q')

    # Get top and featured blogs first
   
    featured_blogs = Blog.objects.filter(featured=True).order_by('-created_at')

    # Exclude top + featured blogs from recent
    recent_blogs = Blog.objects.exclude(
       
        Q(id__in=featured_blogs.values_list('id', flat=True))
    ).order_by('-created_at')

    # Filter all sections by title if searching
    if query:
       
        featured_blogs = featured_blogs.filter(title__icontains=query)
        recent_blogs = recent_blogs.filter(title__icontains=query)

    return render(request, 'home.html', {
        
        'featured_blogs': featured_blogs,
        'recent_blogs': recent_blogs,
    })


# ✅ Blogs by category/type (Education, Travel, etc.)
def blogs_by_type(request, type):
    blogs = Blog.objects.filter(type__iexact=type).order_by('-created_at')
    return render(request, 'category_blogs.html', {
        'blogs': blogs,
        'category': type.capitalize()
    })
