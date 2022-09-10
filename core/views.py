from django.shortcuts import render, HttpResponse
from .models import Client, Order
from .forms import *
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView




class InfoListView(ListView):
    model = Client
    template_name = 'info.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_info.html"


class OrdersListView(ListView):
    model = Order
    template_name = 'order_list.html'


class CreateOrderView(View):
    def post(self, request):
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.description = data["description"]
        order.save()
        return HttpResponse("Форма обработана")

    def get(self, request):
        return render(request, 'clients/order_form.html')



class CreateOrderDjangoFormView(CreateView):
    model = Order
    template_name = 'order_djangoform.html'
    fields = ["name", 'contacts', 'description']
    success_url = '/orders/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['our_number'] = 7
        return context


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/clients/'


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    fields = ['name', 'contacts', 'description']
    success_url = '/orders/'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_info.html'
