"""
ASGI config for little_lemon_restaurant_web_application project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'little_lemon_restaurant_web_application.settings')

application = get_asgi_application()
