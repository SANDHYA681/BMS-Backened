from django.urls import path
from blog.views import home, blogs_by_type

urlpatterns = [
    path('', home, name='home'),
    path('category/<str:type>/', blogs_by_type, name='blogs_by_type'),
]
