from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', RedirectView.as_view(url='/admin/', permanent=True)),

    # Main app (home, blog, services, contact, etc.)
    path('', include('myapp.urls')),

    # Authentication routes
    path('auth/', include('main.urls')),
]

# Serve MEDIA files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
