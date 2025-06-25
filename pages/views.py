from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['titulo', 'contenido']
    template_name = 'pages/create.html'
    success_url = reverse_lazy('page-list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('page-list')
