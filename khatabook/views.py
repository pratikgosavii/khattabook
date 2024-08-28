from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from django.db.models import Sum

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from main.models import *

from datetime import date

from datetime import datetime
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib import messages




@login_required(login_url='login')
def dashboard(request):

    data = customer.objects.all().order_by('name')
    customer_count = data.count()

    context = {
        'data': data,
        'customer_count': customer_count
    }
    return render(request, 'dashboard.html', context)