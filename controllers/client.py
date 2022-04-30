#!/usr/bin/env python
import helloworld
import asyncio
import websockets

async def connect_and_keep_alive():
    uri = "ws://18.144.75.162:8080/"
    timeout = 10
    async with websockets.connect(uri) as websocket:
        msg = "register Teddy Bear"
        await websocket.send(msg)

        res = await websocket.recv()
        print(res)

        while True:
            try:
                res = await asyncio.wait_for(websocket.recv(), timeout)
                if res == "shutdown":
                    break
                # TODO: manage different responses
                else:
                    helloworld.control(res)
                print(res)
            except:
                # Send request to ws server here...
                await websocket.send("path")

async def main():
    websocket_task = asyncio.create_task(connect_and_keep_alive())
    bot_task = asyncio.create_task(helloworld.loop())

    await websocket_task
    await bot_task

asyncio.run(main())
