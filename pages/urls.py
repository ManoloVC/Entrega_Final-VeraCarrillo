from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageDeleteView,ArchivoListView, ArchivoCreateView

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('create/', PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
    path('archivos/', ArchivoListView.as_view(), name='archivo-list'),
    path('archivos/nuevo/', ArchivoCreateView.as_view(), name='archivo-create'),
]
