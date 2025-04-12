from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Blog


class BlogPageView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    paginate_by = 2

    # Search function
    def get_queryset(self):
        queryset = Blog.objects.all()
        query = self.request.GET.get('q', '')

        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(body_text__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
