from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=256)
    body_text = models.TextField(max_length=5000)
    slug = models.SlugField(unique=True, blank=True)
    blog_picture = models.ImageField(upload_to='blogs/', default='blogs/default_blog.jpeg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class BlogReaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    REACTION_CHOICES = [
        (LIKE, 'like'),
        (DISLIKE, 'dislike')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=7, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'blog')


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
