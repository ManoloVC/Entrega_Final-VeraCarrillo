from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Page
from django.db.models import Q
from .models import ArchivoTecnico
from .forms import ArchivoTecnicoForm

class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(autor__username__icontains=query)
            )
        return queryset

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

class ArchivoListView(ListView):
    model = ArchivoTecnico
    template_name = 'pages/archivos_list.html'
    context_object_name = 'archivos'

class ArchivoCreateView(LoginRequiredMixin, CreateView):
    model = ArchivoTecnico
    form_class = ArchivoTecnicoForm
    template_name = 'pages/archivos_form.html'
    success_url = reverse_lazy('archivo-list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
