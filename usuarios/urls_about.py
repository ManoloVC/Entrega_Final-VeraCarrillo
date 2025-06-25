from django.urls import path
from .views_about import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]
