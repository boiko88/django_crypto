from django.db import models
from django.contrib.auth import get_user_model
from geopy.geocoders import Nominatim

import folium

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default_profile.jpeg')
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True, default='Singapore')
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
        return '<p>No location data available.</p>'

    def save(self, *args, **kwargs):
        # If address exists and lat/lng is not manually set
        if self.address and (self.latitude is None or self.longitude is None):
            geolocator = Nominatim(user_agent='django_folium_app')
            location = geolocator.geocode(self.address)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)


class Mentor(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='mentor_profile')
    expertise = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    blog_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.profile.user.username} - Mentor"

    def increment_blog_count(self):
        self.blog_count += 1
        self.save()

    def decrement_blog_count(self):
        if self.blog_count > 0:
            self.blog_count -= 1
            self.save()
