# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from prestamos_app import views

urlpatterns = [
    url(r'^solicitud_prestamos/$', views.PrestamosCreateView.as_view(),
        name='solicitud_prestamos'),
]
