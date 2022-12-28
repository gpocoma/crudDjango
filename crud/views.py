from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Cliente


def index_view(request):
    return render(request, 'index.html', {})


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 20
    template_name = 'crud/cliente_list.html'

    def get_queryset(self):
        return Cliente.objects.order_by('nombre')


class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'crud/cliente_create_form.html'
    success_url = reverse_lazy('read_view')


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'crud/cliente_update_form.html'
    success_url = reverse_lazy('read_view')


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('read_view')
    template_name = 'crud/cliente_delete_form.html'
