from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    path('usuarios/', include('usuarios.urls')),
    path('pages/', include('pages.urls')),
    path('about/', include('usuarios.urls_about')),  # veremos esto más abajo
]
