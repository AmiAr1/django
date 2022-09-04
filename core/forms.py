from django import forms
from clients.models import Order, Client


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", 'contacts', 'description']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address']


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']


class OrderDeleteForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'contacts', 'description']