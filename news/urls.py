from django.urls import path
from .views import NewsPageView


urlpatterns = [
    path('news', NewsPageView.as_view(), name='news'),
]
