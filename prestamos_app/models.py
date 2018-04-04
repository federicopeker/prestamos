# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Prestamos(models.Model):

    dni = models.PositiveIntegerField()
    nombre_apellido = models.CharField(max_length=64)
    genero = models.CharField(max_length=2, choices=(('F', 'F'), ('M', 'M')))
    email = models.EmailField()
    monto = models.PositiveIntegerField()
