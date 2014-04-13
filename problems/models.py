from django.db import models


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

