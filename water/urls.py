"""water URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from clients.views import contacts, about, client_list
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', contacts),
    path('', about),
    path('clients/', client_list),
    path('info/', InfoListView.as_view(), name='info-list'),
    path('client/<int:id>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/update/<int:id>/', ClientUpdateView.as_view(), name="client-update"),
    path('order/delete/<int:id>/', OrderDeleteView.as_view(), name='order-delete'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-info'),
    path('order/create/', CreateOrderView.as_view(), name='create-order'),
    path('order/djangoform/', CreateOrderDjangoFormView.as_view(), name='order-djangoform'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# git init
# git add README.md
# git commit -m "first commit"
#
# git remote add origin https://github.com/AmiAr1/hw4-5.git
# git push -u origin main