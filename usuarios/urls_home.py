from django.urls import path
from .views_home import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
