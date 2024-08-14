import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput
from django import forms

from .models import *
from .forms import *




class customer_filter(django_filters.FilterSet):

    name = django_filters.ModelChoiceFilter(
        queryset=customer.objects.all(),
       widget=forms.Select(
            attrs={
                'class' : 'form-control sele',
                'id' : 'employee'
            })
    )

    
    class Meta:
        model = customer
        fields = '__all__'
       
   

