# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from prestamos_app import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^solicitud_prestamos/$', views.PrestamosCreateView.as_view(),
        name='solicitud_prestamos'),
    url(r'^accounts/login/$', views.login_view, name='login'),
    url(r'^accounts/logout/$', auth_views.logout,
        {'next_page': '/accounts/login/'}, name="logout"),
    url(r'^prestamos/list/$',
        login_required(views.PrestamosListView.as_view()),
        name='prestamos_list'),
]
