from django.test import TestCase
from django.test.client import Client

from problems import graph
from problems.models import *

from users.tests import Factory as UserFactory

import random
import string


class Factory:
	def produce_language_family():
		language_family = LanguageFamily()
		language_family.name = "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
		language_family.slug = "".join(random.choice(string.ascii_letters) for i in range(random.randrange(5,25)))
		language_family.save()
		return language_family
	
	def produce_language(language_family=None):
		language = Language()
		language.name = "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
		language.slug = "".join(random.choice(string.ascii_letters) for i in range(random.randrange(5,25)))
		if language_family:
			language.family = language_family
		else:
			language.family = Factory.produce_language_family()
		language.description = "".join(random.choice(string.printable) for i in range(random.randrange(5,500)))
		language.save()
		return language
	
	def produce_problem(language=None):
		problem = Problem()
		problem.slug = "".join(random.choice(string.ascii_letters) for i in range(random.randrange(5,25)))
		problem.title = "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
		if language:
			problem.language = language
		else:
			problem.language = Factory.produce_language()
		problem.author = "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
		problem.source = "".join(random.choice(string.printable) for i in range(random.randrange(5,25)))
		problem.text = "".join(random.choice(string.printable) for i in range(random.randrange(5,500)))
		problem.save()
		for i in range(random.randrange(4,20)):
			Factory.produce_challenge(problem)
		return problem
	
	def produce_challenge(problem):
		challenge = Challenge()
		challenge.problem = problem
		challenge.challenge = "".join(random.choice(string.ascii_letters) for i in range(random.randrange(5,25)))
		challenge.answer = "".join(random.choice(string.ascii_letters) for i in range(random.randrange(5,25)))
		challenge.save()
		return challenge
	
	def produce_attempt(user, problem, is_successful=False):
		attempt = Attempt()
		attempt.user = user
		attempt.problem = problem
		attempt.is_successful = is_successful
		attempt.save()
		return attempt


class GraphTestCase(TestCase):
	def test_one(self):
		"""
		Tests the Graph's capability to order its nodes (1).
		"""
		g = graph.Graph({
			'A': [],
			'B': ['A'],
			'C': [],
			'D': ['C'],
			'E': ['A'],
			'F': ['D', 'E', 'G'],
			'G': []
		})
		self.assertEqual(g.get_ordered_nodes(), [
			{'A', 'C', 'G'},
			{'B', 'E', 'D'},
			{'F', }
		])
	
	def test_two(self):
		"""
		Tests the Graph's capability to order its nodes (2).
		"""
		g = graph.Graph({
			'A': [],
			'B': ['A'],
			'C': ['B'],
			'D': ['B'],
			'E': ['C'],
			'F': ['C', 'D'],
			'G': ['D']
		})
		self.assertEqual(g.get_ordered_nodes(), [
			{'A', },
			{'B', },
			{'C', 'D'},
			{'E', 'F', 'G'},
		])


class ListTestCase(TestCase):
	def test_unauthenticated(self):
		for i in range(random.randrange(5,50)):
			Factory.produce_problem()
		client = Client()
		response = client.get('/problems/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['problems']), Problem.objects.count())
		self.assertEqual(len(response.context['problems_solved_by_user']), 0)
	
	def test_authenticated(self):
		user, password = UserFactory.produce_user()
		count_solved = 0
		for i in range(random.randrange(5,50)):
			problem = Factory.produce_problem()
			for j in range(random.randrange(0,10)):
				is_successful = random.choice([True, False, False, False])
				Factory.produce_attempt(user, problem, is_successful)
				if is_successful:
					count_solved += 1
					break
		client = Client()
		client.login(email=user.email, password=password)
		response = client.get('/problems/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['problems']), Problem.objects.count())
		self.assertEqual(len(response.context['problems_solved_by_user']), count_solved)


class SingleTestCase(TestCase):
	def test_unauthenticated(self):
		problem = Factory.produce_problem()
		client = Client()
		post = {}
		challenges = Challenge.objects.filter(problem=problem).order_by('?')[:4]
		i = 1
		for challenge in challenges:
			post['challenge_'+str(i)] = challenge.challenge
			post['challenge_'+str(i)+'_answer'] = challenge.answer
			i += 1
		response = client.post('/problems/'+ problem.slug +'/', post)
		self.assertEqual(response.status_code, 404)
	
	def test_right(self):
		problem = Factory.produce_problem()
		user, password = UserFactory.produce_user()
		client = Client()
		client.login(email=user.email, password=password)
		post = {}
		challenges = Challenge.objects.filter(problem=problem).order_by('?')[:4]
		i = 1
		for challenge in challenges:
			post['challenge_'+str(i)] = challenge.challenge
			post['challenge_'+str(i)+'_answer'] = challenge.answer
			i += 1
		response = client.post('/problems/'+ problem.slug +'/', post)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['success'], True)
	
	def test_wrong(self):
		problem = Factory.produce_problem()
		user, password = UserFactory.produce_user()
		client = Client()
		client.login(email=user.email, password=password)
		post = {}
		challenges = Challenge.objects.filter(problem=problem).order_by('?')[:4]
		i = 0
		for challenge in challenges:
			post['challenge_'+str(i)] = challenge.challenge
			post['challenge_'+str(i)+'_answer'] = challenge.answer
			i += 1
		wrong = 'challenge_'+ str(random.choice(range(1,5))) +'_answer'
		post[wrong] = post[wrong] + '42'
		response = client.post('/problems/'+ problem.slug +'/', post)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context['success'], False)

