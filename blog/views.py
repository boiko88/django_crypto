from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect

from .models import Blog, BlogReaction, Comment
from .forms import CommentForm


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
        action = request.POST.get('action')  # 'like' or 'dislike'
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)

        try:
            reaction = BlogReaction.objects.get(user=request.user, blog=blog)

            if reaction.reaction == action:
                # If same reaction clicked again, remove it (toggle off)
                reaction.delete()
            else:
                # If different reaction clicked, update it
                reaction.reaction = action
                reaction.save()

        except BlogReaction.DoesNotExist:
            # No reaction exists yet, create new
            BlogReaction.objects.create(user=request.user, blog=blog, reaction=action)

        return redirect('blog')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = self.object
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', slug=self.object.slug)
        return self.render_to_response(self.get_context_data(form=form))
