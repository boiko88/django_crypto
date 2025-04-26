from rest_framework import viewsets, permissions
from blog.models import Blog
from .serializers import BlogSerializer
from .permissions import IsMentorOrAdmin


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        # Only allow mentors/admins to create, update, or delete
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsMentorOrAdmin()]
        # Anyone can view/list
        return [permissions.AllowAny()]
