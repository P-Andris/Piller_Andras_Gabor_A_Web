# Generated by Django 4.2.1 on 2023-05-31 09:18

from django.db import migrations

def feltoltes(apps, schema_editor):
    Kategoria = apps.get_model('vizsga', 'Kategoria')

    kategoriak = ['Sport', 'Történelem']

    for i in range(len(kategoriak)):
        k = Kategoria(i + 1, kategoriak[i])
        k.save()

class Migration(migrations.Migration):

    dependencies = [
        ('vizsga', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(feltoltes)
    ]
