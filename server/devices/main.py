from aiohttp import web
from .sonoff.sonoff import Sonoff


def init_devices(app: web.Application, api_app: web.Application) -> None:
    sonoff = Sonoff()
    sonoff.register(app, api_app)
