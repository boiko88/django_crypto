<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crypto.urls')),
    path('', include('weather.urls')),
    path('', include('news.urls')),
    path('', include('users.urls')),
    path('', include('blog.urls')),
    path('api/', include('blog_api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crypto.urls')),
    path('', include('weather.urls')),
    path('', include('news.urls')),
    path('', include('users.urls')),
    path('', include('blog.urls')),
    path('api/', include('blog_api.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 49c1d749563c4b264d06f2cf3418138d200a600b
