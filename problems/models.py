from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

import json


class LanguageFamily(models.Model):
	name = models.CharField(max_length=240)
	slug = models.SlugField(unique=True)
	
	class Meta:
		verbose_name = "Language Family"
		verbose_name_plural = "Language Families"
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.name


class Language(models.Model):
	name = models.CharField(max_length=240)
	family = models.ForeignKey(LanguageFamily)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=240)
	slug = models.SlugField(unique=True)
	ordering = models.SmallIntegerField()
	
	class Meta:
		ordering = ['ordering']
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.name


class Problem(models.Model):
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=240)
	language = models.ForeignKey(Language, blank=False, null=False)
	tags = models.ManyToManyField(Tag)
	author = models.CharField(max_length=240, blank=False, null=False)
	source = models.CharField(max_length=240, blank=False, null=False)
	text = models.TextField()
	note = models.TextField(blank=True, null=True)
	number_of_challenges = models.PositiveSmallIntegerField(default=4)
	created = models.DateTimeField(auto_now_add=True)
	
	@property
	def count_solved(self):
		"""
		Returns the number of users who have solved the problem.
		"""
		return Attempt.objects.filter(
			problem = self,
			is_successful = True
		).values('user').distinct().count()
	
	@property
	def last_comment(self):
		"""
		Returns the problem's last comment.
		"""
		last_comments = Comment.objects.filter(
			problem = self
		).order_by('created')
		if len(last_comments):
			return last_comments[0]
		else:
			return None
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.slug


class Graph(models.Model):
	json = models.TextField()
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return "The Graph"


class Challenge(models.Model):
	problem = models.ForeignKey(Problem)
	challenge = models.CharField(max_length=240)
	answer = models.CharField(max_length=240)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.problem.slug+': '+self.challenge


class Attempt(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	problem = models.ForeignKey(Problem)
	is_successful = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return str(self.user)+': '+str(self.problem)


class Comment(models.Model):
	problem = models.ForeignKey(Problem)
	parent = models.ForeignKey('self', blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""
		Returns the model's string representation.
		"""
		return self.text

