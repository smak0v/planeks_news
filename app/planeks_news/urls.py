"""
planeks_news URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .admin import admin_site

urlpatterns = [
    path('planeks_news_admin/', admin_site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('users/', include('users.urls')),
    path('', include('news.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'planeks_news.views.error_404_view'
