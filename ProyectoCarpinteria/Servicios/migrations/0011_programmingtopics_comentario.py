# Generated by Django 5.1.1 on 2024-09-06 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0010_remove_programmingtopics_contenido'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtopics',
            name='comentario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
