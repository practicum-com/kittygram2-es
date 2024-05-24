"""
Configuración ASGI para el proyecto kittygram2.

Expone el ASGI que puede llamarse como una variable de nivel módulo llamada ``application``.

Para obtener más información acerca de este archivo, consulta
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kittygram2.settings')

application = get_asgi_application()
