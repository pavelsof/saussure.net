from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

import json


class Problem(models.Model):
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=240)
	text = models.TextField()
	number_of_challenges = models.PositiveSmallIntegerField(default=4)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.slug


class ProblemChallenge(models.Model):
	problem = models.ForeignKey(Problem)
	challenge = models.CharField(max_length=240)
	answer = models.CharField(max_length=240)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.problem.slug+': '+self.challenge


class UserAttempt(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	problem = models.ForeignKey(Problem)
	is_successful = models.BooleanField()
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return str(self.user)+': '+str(self.problem)


class Graph(models.Model):
	json = models.TextField()
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return "The Graph"

