# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from prestamos_app.models import Prestamos


class PrestamosForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ('dni', 'nombre_apellido', 'genero', 'email', 'monto')

        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_apellido': forms.TextInput(
                attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PrestamoUpdateForm(forms.ModelForm):
    class Meta:
        model = Prestamos
        fields = ('dni', 'nombre_apellido', 'genero', 'email', 'monto',
                  'aprobado', 'error')

        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_apellido': forms.TextInput(
                attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control'}),
        }
