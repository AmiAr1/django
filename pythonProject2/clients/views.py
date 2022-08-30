from django.shortcuts import render, HttpResponse
from .models import Client



def contacts(request):
    return render(request, 'clients/contacts.html')


def about(request):
    return render(request, 'about.html')


def client_list(request):
    context = {}
    clients_list = Client.objects.all()
    context['clients_list'] = clients_list
    html_page = render(request, 'name.html', context)
    return html_page