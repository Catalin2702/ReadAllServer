import asyncio
import websockets
import json
import requests

url = 'http://192.168.1.3:8085/api/'

request_map = {
	'search': url + 'search',
	'getChapter': url + 'get_chapter',

	'getNovelContent': url + 'get_content/novel',
	'getMangaContent': url + 'get_content/manga',
}


async def server(websocket, path):
	try:
		while True:
			message = await websocket.recv()
			try:
				message = json.loads(message)
				if message.get('action', False) and message.get('query', False):
					content_type = '&content_type=' + message.get('contentType') if message.get('contentType') else ''
					url_req = request_map.get(message.get('action')) + '?query=' + message.get('query') + content_type
					response = requests.get(url_req)
					if response.status_code == 200:
						await websocket.send(response.text)
				else:
					print('Richiesta errata')

			except json.decoder.JSONDecodeError:
				pass

	except websockets.exceptions.ConnectionClosed:
		pass


start = websockets.serve(server, "192.168.1.3", 8000)

asyncio.get_event_loop().run_until_complete(start)
asyncio.get_event_loop().run_forever()
