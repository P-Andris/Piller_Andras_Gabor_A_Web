from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Kategoria, Teszt
from .filters import TesztFilter

# tesztek/
def tesztek(request):
    tesztek = Teszt.objects.all()

    # tesztek/kategoria/{id}/
    tesztfilter = TesztFilter(request.GET, queryset = tesztek)

    context = {
        'tesztek': tesztek,
        'tesztfilter': tesztfilter
    }

    return render(request, 'tesztek.html', context = context)

# kategoria/
def kategoriak(request):
    kategoriak = Kategoria.objects.all()
    
    context = {
        'kategoriak': kategoriak
    }

    return render(request, 'kategoriak.html', context = context)