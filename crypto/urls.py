<<<<<<< HEAD
from django.urls import path
from .views import CryptoPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('crypto/', CryptoPageView.as_view(), name='crypto'),
=======
from django.urls import path
from .views import CryptoPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('crypto/', CryptoPageView.as_view(), name='crypto'),
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
]