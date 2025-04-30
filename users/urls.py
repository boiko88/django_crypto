<<<<<<< HEAD
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegisterView, ProfileView

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
=======
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CustomRegisterView, ProfileView

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
