from MySQL import MySQL
from utils import ERROR_MESSAGE


class Account:

	__username = None
	__email = None
	__token = None
	__password = None

	def __init__(self, kwargs):
		if kwargs:
			self.__username = kwargs.get('username')
			self.__token = kwargs.get('token')
			self.__password = kwargs.get('password')

	def get_username(self):
		return self.__username

	def get_email(self):
		return self.__email

	def get_token(self):
		return self.__token

	def _get_password(self):
		return self.__password

	def __check_token(self):
		query = """
		select s.token_secret as token, s.valid_secret as valid,
			s.updatetime_secret as time
		from secrets s
		join users u on s.id_user = u.id_user
		where u.username_user = '{user}' and s.token_secret = '{token}'
		""".format(user=self.__username, token=self.__token)

		results = MySQL().query(query)

		print(results)

	def sign_in(self):
		query = """
		select u.username_user as username, s.pw_secret as password,
			u.email_user as email
		from users u
		join secrets s on u.id_user = s.id_user
		where u.username_user = '{user}' and s.pw_secret = '{password}'
		""".format(user=self.__username, password=self.__password)

		results = MySQL().query(query)

		if results:
			self.__email = results[0]['email']

		return True if results else False

	def register(self):
		# check email/username existence
		query = """
		select u.username_user as username, u.email_user as email
		from users u
		where u.username_user = '{username}' or u.email_user = '{email}'
		""".format(username=self.__username, email=self.__email)

		results = MySQL().query(query)

		print(results)

		if results:
			return False, ERROR_MESSAGE['EMAIL_EXISTS']

		insert_new_user = """
		insert into users(email_user, username_user, updatetime_user)
		value ({email}, {username}, now());
		""".format(email=self.__email, username=self.__username)
		return True, ''
