from users.models import Profile, Mentor


def is_mentor(request):
    user = request.user
    is_mentor = False
    if user.is_authenticated:
        try:
            profile = Profile.objects.get(user=user)
            is_mentor = Mentor.objects.filter(profile=profile, is_active=True, approved=True).exists() or user.is_staff
        except Profile.DoesNotExist:
            is_mentor = user.is_staff
    return {'is_mentor': is_mentor}
