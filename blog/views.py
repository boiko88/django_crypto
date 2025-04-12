from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

from .models import Blog, BlogReaction


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

        # Add the like and dislike counts to each blog
        for blog in context['blogs']:
            blog.likes_count = blog.blogreaction_set.filter(reaction='like').count()
            blog.dislikes_count = blog.blogreaction_set.filter(reaction='dislike').count()

        return context

    # Handle Like/Dislike action directly on the list page
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)

        # Check if the user already has a reaction to the blog
        reaction_exists = BlogReaction.objects.filter(user=request.user, blog=blog).exists()

        if not reaction_exists:
            # Create a new reaction
            if action == 'like':
                BlogReaction.objects.create(user=request.user, blog=blog, reaction=BlogReaction.LIKE)
            elif action == 'dislike':
                BlogReaction.objects.create(user=request.user, blog=blog, reaction=BlogReaction.DISLIKE)

        return redirect('blog')


# class BlogDetailView(LoginRequiredMixin, DetailView):
#     model = Blog
#     template_name = 'blog_detail.html'
#     context_object_name = 'blog'
#
#     def post(self, request, *args, **kwargs):
#         blog = self.get_object()
#         action = request.POST.get('action')
#
#         # Check if the user already has a reaction to the blog
#         reaction_exists = BlogReaction.objects.filter(user=request.user, blog=blog).exists()
#
#         if not reaction_exists:
#             # Create a new reaction
#             if action == 'like':
#                 BlogReaction.objects.create(user=request.user, blog=blog, reaction=BlogReaction.LIKE)
#             elif action == 'dislike':
#                 BlogReaction.objects.create(user=request.user, blog=blog, reaction=BlogReaction.DISLIKE)
#
#         return redirect('blog_detail', pk=blog.pk)
