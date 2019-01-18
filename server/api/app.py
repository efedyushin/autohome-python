from aiohttp import web


def make_api_app(main_app: web.Application) -> web.Application:
    api_app = web.Application()
    api_app['config'] = main_app['config']
    api_app['main_app'] = main_app
    return api_app
