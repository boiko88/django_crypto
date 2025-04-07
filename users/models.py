from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    # name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"
