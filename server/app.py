
from aiohttp import web

from .api.app import make_api_app
from .devices.main import init_devices
from .utils.config import init_config


def make_app(config: dict = {}) -> web.Application:
    app = web.Application()
    init_config(app)
    api_app = make_api_app(app)
    init_devices(app, api_app)
    return app
