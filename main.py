import asyncio
import websockets
from websockets.exceptions import ConnectionClosed
import json
from mapping import api_url, api_request_map, actions_map
from services import Account


account = Account


async def server(websocket, path):
	try:
		while True:
			message = await websocket.recv()
			try:
				kwargs = json.loads(message)
				kwargs['url'] = api_url
				kwargs['api_request_map'] = api_request_map
				kwargs['account'] = account
				response = actions_map[kwargs.get('action', 'default')](kwargs)
				if response:
					await websocket.send(json.dumps(response))
				else:
					await websocket.send('')

			except json.decoder.JSONDecodeError:
				pass

	except ConnectionClosed:
		pass


start = websockets.serve(server, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start)
asyncio.get_event_loop().run_forever()
