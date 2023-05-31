from django.db import models

from django.db import models

VALASZOK = [
    'v1', 'v2', 'v3', 'v4'
]

class Kategoria(models.Model):
    # id kulcsot alapból létrehozza
    kategorianev = models.CharField(max_length = 40, unique = True, verbose_name = 'Kategória neve')
    
    def __str__(self):
        return self.kategorianev

class Teszt(models.Model):
    # id kulcsot alapból létrehozza
    kerdes = models.CharField(max_length = 150, unique = True, verbose_name = 'Kérdés')
    v1 = models.CharField(max_length = 150, verbose_name = '1. válasz')
    v2 = models.CharField(max_length = 150, verbose_name = '2. válasz')
    v3 = models.CharField(max_length = 150, verbose_name = '3. válasz')
    v4 = models.CharField(max_length = 150, verbose_name = '4. válasz')
    helyes = models.CharField(max_length = 150, default = v1, verbose_name = 'Helyes válasz')
    kategoria_id = models.ForeignKey(Kategoria, on_delete = models.CASCADE, verbose_name = 'Kategória')

    def __str__(self):
        return self.kerdes