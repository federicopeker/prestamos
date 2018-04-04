# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from prestamos_app.models import Prestamos
from django.views.generic import CreateView
from prestamos_app.forms import PrestamosForm


class PrestamosCreateView(CreateView):
    model = Prestamos
    template_name = 'solicitud_prestamos.html'
    form_class = PrestamosForm

    def get_success_url(self):
        return reverse('solicitud_prestamos')
