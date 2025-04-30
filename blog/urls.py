<<<<<<< HEAD
from django.urls import path
from .views import BlogPageView, BlogDetailView


urlpatterns = [
    path('blog', BlogPageView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
=======
from django.urls import path
from .views import BlogPageView, BlogDetailView


urlpatterns = [
    path('blog', BlogPageView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
