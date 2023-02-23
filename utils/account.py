from MySQL import MySQL
from constants import ERROR_MESSAGE


class Account:

	username = None
	email = None
	__token = None
	__password = None

	def __init__(self, **kwargs):
		if kwargs:
			self.username = kwargs.get('username')
			self.__token = kwargs.get('token')
			if self.__token:
				self.__check_token()

	def __check_token(self):
		query = """
		select s.token_secret as token, s.valid_secret as valid,
			s.updatetime_secret as time
		from secrets s
		join users u on s.id_user = u.id_user
		where u.username_user = '{user}' and s.token_secret = '{token}'
		""".format(user=self.username, token=self.__token)

		results = MySQL().query(query)

		print(results)

	def sign_in(self):
		query = """
		select u.username_user as username, s.pw_secret
		from users u
		join secrets s on u.id_user = s.id_user
		where u.username_user = '{user}' and s.pw_secret = '{password}'
		""".format(user=self.username, password=self.__password)

		results = MySQL().query(query)

		print(results)

	def register(self):
		# check email existence
		query = """
		select u.username_user as username, u.email_user as email
		from users u
		where u.username_user = '{username}' or u.email_user = '{email}'
		""".format(username=self.username, email=self.email)

		results = MySQL().query(query)

		print(results)

		if results:
			return False, ERROR_MESSAGE['EMAIL_EXISTS']
