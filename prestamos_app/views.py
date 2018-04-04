# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from prestamos_app.models import Prestamos
from django.views.generic import CreateView
from prestamos_app.forms import PrestamosForm
from prestamos_app.prestamos_service import PrestamosServices


class PrestamosCreateView(CreateView):
    model = Prestamos
    template_name = 'solicitud_prestamos.html'
    form_class = PrestamosForm

    def form_valid(self, form):
        self.object = form.save()
        prestamos_service = PrestamosServices()
        resultado = prestamos_service.consulta_prestamos(self.object)
        if resultado['approved']:
            aprobado = "aprobado"
        else:
            aprobado = "rechazado"

        message = 'El prestamo fue {0} '.format(aprobado)
        if resultado['error']:
            message += " y contiene errores"

        messages.add_message(
            self.request,
            messages.INFO,
            message,
        )
        return super(PrestamosCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('solicitud_prestamos')
