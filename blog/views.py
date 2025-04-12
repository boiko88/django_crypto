from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Blog


class BlogPageView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 2
