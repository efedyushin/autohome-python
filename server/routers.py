from aiohttp import web
from .devices.sonoff.handlers import sonoff_web_socket_handler


def init_routers(app: web.Application) -> None:
    app.add_routes([web.get('/devices', sonoff_web_socket_handler)])
