<<<<<<< HEAD
from django.urls import path
from .views import NewsPageView


urlpatterns = [
    path('news', NewsPageView.as_view(), name='news'),
]
=======
from django.urls import path
from .views import NewsPageView


urlpatterns = [
    path('news', NewsPageView.as_view(), name='news'),
]
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
