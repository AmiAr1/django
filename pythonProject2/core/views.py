from django.shortcuts import render
from .models import Client


# Create your views here.
def info_list(request):
    context={}
    context['info_list'] = Client.objects.all()
    return render(request, 'info.html', context)


# def client_detail(request, id=id)