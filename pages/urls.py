from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageDeleteView

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page-detail'),
    path('create/', PageCreateView.as_view(), name='page-create'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
]
