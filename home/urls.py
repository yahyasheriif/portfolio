from django.contrib import admin
from django.urls import path
from .views import home_view, send_email
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home_views'),
    path('contact/', send_email, name='send_email'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
