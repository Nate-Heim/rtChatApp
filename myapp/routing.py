# Nate Heim
# myapp/routing.py

from django.urls import path
from myapp.consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
]
