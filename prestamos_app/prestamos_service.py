# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Modulo donde se va gestionar las consultas con la api
http://scoringservice.moni.com.ar:7001/api/v1/scoring/
"""

import requests


class PrestamosServices():

    def consulta_prestamos(self, prestamo):
        """
        Consulta en la api si el prestamos se aprueba o no
        :param prestamo: prestamo el cual se va consultar
        :return: un json si se aprueba y si hay un error
        """
        url = "http://scoringservice.moni.com.ar:7001/api/v1/scoring/?document_number={0}&gender={1}&email={2}&monto={3}"
        url = url.format(prestamo.dni, prestamo.genero, prestamo.email,
                         prestamo.monto)
        request = requests.get(url)
        return request.json()
