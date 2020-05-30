from django.contrib import admin
from django.urls import path
from django.urls import include
from decouple import config
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('advogado/', include('back.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)