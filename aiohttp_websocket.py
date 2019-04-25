import asyncio
import time
import json
import datetime
import logging
import sys

import aiohttp
from aiohttp import web

def create_loop():
    return asyncio.get_event_loop()

# loop = create_loop()


aa = int(time.time())

routes = web.RouteTableDef()

@routes.get('/echo')
async def wshandle(request):
    print("1")
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(2)
    async for msg in ws:
        # print(msg.type)
        print(msg, 'msg')
        if msg.type == web.WSMsgType.text:
            await ws.send_str("Hello, {}".format(msg.data))
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws

async def run():
    print("run 1")
    await asyncio.sleep(15)
    print("run done")

@routes.get('/')
async def index(request):
    print('ok', '\t\t...')
    loop = asyncio.get_event_loop()
    task = loop.create_task(run())
    return web.Response(text="ok.")

async def init(routes):
    app = web.Application()
    app['sockets'] = []
    app.add_routes(routes)
    return app


# loop.run_until_complete(init(loop, routes))
# loop.run_forever()
app = init(routes)
web.run_app(app, host="0.0.0.0", port=8005)

