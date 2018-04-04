# prestamos

Aplicacion de prestamos desarrollado con Python 2.7 y Django 1.11.12

Solucion echa con sqlite

Armado de solucion:

- $ virtualenv -p python2.7 virtualenv
- $ . virtualenv/bin/activate
- $ pip install -r requirements.txt

Urls:
- /solicitud_prestamos/
- Login de sitio administrativo: /accounts/login/
- Listados de prestamos: /prestamos/list/

Los usuarios deben ser creado por consola con el comando createsuperuser del
manage.py