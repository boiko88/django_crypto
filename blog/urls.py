from django.urls import path
from .views import BlogPageView, BlogDetailView


urlpatterns = [
    path('blog', BlogPageView.as_view(), name='blog'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
