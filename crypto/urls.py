from django.urls import path
from .views import CryptoPageView, HomePageView

urlpatterns = [
    path('', CryptoPageView.as_view(), name='crypto'),  # This will handle the root '/'
    path('home/', HomePageView.as_view(), name='home'),  # This will handle '/home/'
]