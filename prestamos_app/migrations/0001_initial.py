# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-04 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.PositiveIntegerField()),
                ('nombre_apellido', models.CharField(max_length=64)),
                ('genero', models.CharField(choices=[('F', 'F'), ('M', 'M')], max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('monto', models.PositiveIntegerField()),
            ],
        ),
    ]
