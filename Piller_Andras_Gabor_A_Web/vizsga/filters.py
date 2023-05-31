import django_filters as filters
from .models import Kategoria, Teszt
from django import forms

class TesztFilter(filters.FilterSet):
    kategoria_id = filters.ModelChoiceFilter(
        label = 'Kategória',
        field_name = 'kategoria_id_id',
        queryset = Kategoria.objects.all(),
        widget = forms.Select(attrs = {'class': 'form-control'})
    )

    class Meta:
        model = Teszt
        fields = ['kategoria_id']