# Generated by Django 5.1.1 on 2024-09-06 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0004_programmingtopics'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtopics',
            name='desarrollo',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'En Proceso'), (3, 'Completado')], default=1),
        ),
    ]
