from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from bms import views

auth_urlpatterns = [
    path('log-in/', views.loginPage),
    path('sign-up/', views.signupPage),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutUS),
    path('add-blog/', views.addBlogUser),
    path('blogs/', views.blog),
    path('home/', views.home),
    path('add-blog-admin/', views.addBlogAdmin),
    path('update-blog-admin/', views.updateBlogAdmin),
    path('view-blog-list/', views.blogListAdmin),
    path('auth/', include(auth_urlpatterns)),
    
    # Home and category 
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
