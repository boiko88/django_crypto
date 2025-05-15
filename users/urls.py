from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegisterView, ProfileView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
