from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from bms import views
from addBlogs import views as blog_views
from users import views as user_views

# Serve static files during development
auth_urlpatterns = [
    path('log-in/', user_views.loginUser, name='login'),
    path('sign-up/', user_views.signupUser),
    path('logout/', user_views.logoutUser)
]

# Static files (CSS, JavaScript, Images)
blog_urlpatterns = [
    path('add-blog/', blog_views.addBlogs, name='addBlog'),
    path('view-blogs/', blog_views.my_blogs, name='viewBlogs'),
    path('blogs/', blog_views.blog),
    path('<int:id>', blog_views.blogDetails),  
    path('<int:id>/edit-blog/', blog_views.editBlogPage, name='edit_blogPage'),
    path('<int:id>/edit/', blog_views.editBlog, name='edit_blog'),
    
    #  ADD blogs_by_type and any other missing routes
    path('category/<str:type>/', blog_views.blogs_by_type, name='blogs_by_type'),
]

urlpatterns = [
    path('', views.landingPage),
    path('', blog_views.home, name='home'),
    path('admin/', admin.site.urls),
    
    path("home/", blog_views.home, name='home'),  

    path('sign-up/', views.signupPage),
    path('user-profile/', views.profilePage),
    path('contact-us/', views.contactUs),
    path('add-blog-admin/', views.addBlogAdmin),
    path('update-blog-admin/', views.updateBlogAdmin),
    path('view-blog-list/', views.blogListAdmin),
    path('user-profile/', views.profilePage),
    path("edit-user", views.editUserProfile),

    path('auth/', include(auth_urlpatterns)),
    path('blogs/', include(blog_urlpatterns)),
    path('about-us/', include('about.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
