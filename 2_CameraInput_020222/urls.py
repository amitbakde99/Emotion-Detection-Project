from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='emotion_det'),
    path('facecam_feed/',views.facecam_feed, name='facecam_feed_emodet'),
    path('stopcam_feed/',views.stopcam_feed, name='stopcam_feed_emodet'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)