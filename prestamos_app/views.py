# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.core.urlresolvers import reverse
from prestamos_app.models import Prestamos
from django.views.generic import CreateView
from prestamos_app.forms import PrestamosForm
from prestamos_app.prestamos_service import PrestamosServices
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse


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


def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, user)
            if user.is_staff:
                return HttpResponseRedirect(reverse('solicitud_prestamos'))
            else:
                message = 'El usuario no es un administrador'
                messages.add_message(
                    request,
                    messages.INFO,
                    message,
                )
                return HttpResponseRedirect(reverse('logout'))

    else:
        form = AuthenticationForm(request)

    context = {
        'form': form,
    }
    template_name = 'login.html'
    return TemplateResponse(request, template_name, context)
