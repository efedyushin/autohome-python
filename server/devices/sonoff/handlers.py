from aiohttp import web


async def sonoff_web_socket_handler(request: web.Request) -> web.WebSocketResponse:
    app = request.app
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    config_answer = {
        "error": 0,
        "reason": "ok",
        "IP": app['config']['IP'],
        "port": app['config']['PORT']
    }
    async for msg in ws:
        if msg.data == 'close':
            app['socket']
            await ws.close()
