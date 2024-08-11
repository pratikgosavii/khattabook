"""nicbussinesscard URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [

    path('view-customer/', view_customer, name='view_customer'),
    path('view-customer-with-id/<customer_id>', view_customer_with_id, name='view_customer_with_id'),
    path('view-customer-payment/<customer_id>', view_customer_payment, name='view_customer_payment'),

    path('add-customer/', add_customer, name='add_customer'),
    path('update-customer/<customer_id>', update_customer, name='update_customer'),
    path('list-customer/', list_customer, name='list_customer'),
    path('delete-customer/<customer_id>', delete_customer, name='delete_customer'),

    path('add-record/<customer_id>', add_record, name='add_record'),
    path('list-record/', list_record, name='list_record'),

    path('add-payment/<customer_id>', add_payment, name='add_payment'),
    path('update-payment/<payment_id>', update_payment, name='update_payment'),
    path('delete-payment/<payment_id>', delete_payment, name='delete_payment'),

  

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
