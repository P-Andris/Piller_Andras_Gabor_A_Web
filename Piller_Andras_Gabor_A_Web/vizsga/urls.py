from django.urls import path
from . import views

urlpatterns = [
    path('tesztek/', views.tesztek, name = 'tesztek'), # Összes teszt kategóriára való szűréssel együtt
    path('kategoria/', views.kategoriak, name = 'kategoriak') # Összes kategória
]
