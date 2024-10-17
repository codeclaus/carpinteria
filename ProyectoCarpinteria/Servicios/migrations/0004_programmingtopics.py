# Generated by Django 5.1.1 on 2024-09-06 23:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_temas_alter_productoslavadora_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammingTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categorias/programming')),
                ('titulo', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servicios.categoria')),
                ('tema', models.ManyToManyField(to='Servicios.temas')),
            ],
            options={
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programaciones',
                'ordering': ['titulo'],
            },
        ),
    ]
