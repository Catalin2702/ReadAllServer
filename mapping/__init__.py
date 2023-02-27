from utils import api_service, sign_in, register, default


api_url = 'http://127.0.0.1:8085/api/'

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
	'signIn': sign_in,
	'register': register,
	'default': default
}
