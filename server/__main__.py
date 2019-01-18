from aiohttp import web

from .app import make_app


def main() -> None:
    app = make_app()
    web.run_app(app, host=app['config']['HOST'],
                port=app['config']['PORT'])


if __name__ == "__main__":
    main()
