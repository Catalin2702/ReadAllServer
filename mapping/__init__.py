from utils import api_service, sign_in, register


api_url = 'http://192.168.1.3:8085/api/'

api_request_map = {
	'search': 'search?',
	'getChapter': 'get_chapter?',
	'getNovelContent': 'get_content/novel?',
	'getMangaContent': 'get_content/manga?',
}

actions_map = {
	'search': api_service,
	'getChapter': api_service,
	'getNovelContent': api_service,
	'getMangaContent': api_service,
	'sign_in': sign_in,
	'register': register,
}
