from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls_home')),  
    path('usuarios/', include('usuarios.urls')),
    path('pages/', include('pages.urls')),
    path('about/', include('usuarios.urls_about')),
    path('archivos/', include('pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)