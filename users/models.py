from django.db import models
from django.contrib.auth import get_user_model

import folium

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default_profile.jpeg')
    email = models.EmailField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def generate_map(self):

        if self.latitude and self.longitude:
            m = folium.Map(location=[self.latitude, self.longitude], zoom_start=10)
            folium.Marker(
                [self.latitude, self.longitude],
                tooltip=f"{self.user.username}'s Location"
            ).add_to(m)
            return m._repr_html_()
        return "<p>No location data available.</p>"
