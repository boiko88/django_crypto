from django.urls import path
from .views import CryptoPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('crypto/', CryptoPageView.as_view(), name='crypto'),
]