from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default_profile.jpg')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
