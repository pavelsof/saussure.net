from django.test import TestCase
from django.test.client import Client

from users.models import User

import random
import string


class Factory:
	def produce_email():
		email = "".join(random.choice(string.ascii_lowercase) for i in range(random.randrange(5,25)))
		email += "@"
		email += random.choice(['gmail.com', 'yahoo.com', 'mail.ru'])
		return email
	
	def produce_password():
		return "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
	
	def produce_user():
		email = Factory.produce_email()
		password = Factory.produce_password()
		user = User.objects.create_user(email, password)
		return (user, password)


class RegistrationTestCase(TestCase):
	def test_different_passwords(self):
		client = Client()
		count_before = User.objects.count()
		email = Factory.produce_email()
		string_one = Factory.produce_password()
		while True:
			string_two = Factory.produce_password()
			if string_one != string_two:
				break
		response = client.post('/users/registration/', {
			'email': email,
			'password': string_one,
			'password2': string_two
		})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['message'], "The two passwords do not match.")
		self.assertEqual(User.objects.count(), count_before)
	
	def test_registration(self):
		client = Client()
		email = Factory.produce_email()
		password = Factory.produce_password()
		response = client.post('/users/registration/', {
			'email': email,
			'password': password,
			'password2': password
		})
		self.assertEqual(response.status_code, 302)
		user = User.objects.latest(field_name='created')
		self.assertEqual(user.email, email)
	
	def test_registration_with_name(self):
		client = Client()
		email = Factory.produce_email()
		password = Factory.produce_password()
		name = Factory.produce_password()
		response = client.post('/users/registration/', {
			'email': email,
			'password': password,
			'password2': password,
			'name': name
		})
		self.assertEqual(response.status_code, 302)
		user = User.objects.latest(field_name='created')
		self.assertEqual(user.email, email)
		self.assertEqual(user.name, name)


class LoginTestCase(TestCase):
	def test_invalid_login(self):
		client = Client()
		email = Factory.produce_email()
		password = Factory.produce_password()
		response = client.post('/users/login/', {
			'email': email,
			'password': password
		})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['message'], "No such user.")
	
	def test_login(self):
		client = Client()
		email = Factory.produce_email()
		password = Factory.produce_password()
		User.objects.create_user(email, password)
		response = client.post('/users/login/', {
			'email': email,
			'password': password
		})
		self.assertEqual(response.status_code, 302)
	
	def test_404(self):
		client = Client()
		email = Factory.produce_email()
		password = Factory.produce_password()
		User.objects.create_user(email, password)
		client.login(email=email, password=password)
		response = client.post('/users/login/', {})
		self.assertEqual(response.status_code, 404)


class ProfileTestCase(TestCase):
	pass

