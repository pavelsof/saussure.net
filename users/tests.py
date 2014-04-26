from django.test import TestCase
from django.test.client import Client

import uuid


class RegistrationTestCase(TestCase):
	def test_different_passwords(self):
		c = Client()
		string_one = uuid.uuid4()
		while True:
			string_two = uuid.uuid4()
			if string_one != string_two:
				break
		response = c.post('/users/registration/', {
			'email': 'mail@yatdesign.com',
			'password': string_one,
			'password2': string_two
		})
		self.assertEqual(response.status_code, 200)


class LoginTestCase(TestCase):
	pass


class ProfileTestCase(TestCase):
	pass

