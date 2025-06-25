from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls_home')),  
    path('usuarios/', include('usuarios.urls')),
    path('pages/', include('pages.urls')),
    path('about/', include('usuarios.urls_about')),
]

