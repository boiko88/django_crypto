from rest_framework import permissions
from users.models import Profile, Mentor


class IsMentorOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow mentors or admins to create, update, or delete blogs.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False
        if user.is_staff:
            return True
        try:
            profile = Profile.objects.get(user=user)
            return Mentor.objects.filter(profile=profile, is_active=True, approved=True).exists()
        except Profile.DoesNotExist:
            return False
