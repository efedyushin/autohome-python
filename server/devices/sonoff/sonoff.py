from aiohttp import web
from server.devices.base import BaseDevice
from .handlers import sonoff_web_socket_handler


class Sonoff(BaseDevice):
    def register(self, app: web.Application, api_app: web.Application) -> None:
        self.app = app
        self.register_routes()

    def register_routes(self) -> None:
        self.app.add_routes([
            web.get('/devices', sonoff_web_socket_handler)  # emulate sonoff ws route for devices
        ])
