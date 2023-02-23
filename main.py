import asyncio
import websockets
import json
from mapping import api_url, api_request_map, actions_map


async def server(websocket, path):
	try:
		while True:
			message = await websocket.recv()
			try:
				message = json.loads(message)
				if message.get('action'):
					if message['action'] in api_request_map:
						message['url'] = api_url
						message['api_request_map'] = api_request_map
						response = actions_map[message['action']](message)
						if response:
							await websocket.send(response)
						else:
							await websocket.send('')
				else:
					print('Richiesta errata')

			except json.decoder.JSONDecodeError:
				pass

	except websockets.exceptions.ConnectionClosed:
		pass


start = websockets.serve(server, "192.168.1.3", 8000)

asyncio.get_event_loop().run_until_complete(start)
asyncio.get_event_loop().run_forever()
