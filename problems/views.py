from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic.base import View

from problems.models import Attempt
from problems.models import Challenge as ChallengeModel
from problems.models import Problem


class List(View):
	def get(self, request):
		"""
		Renders all problems.
		"""
		problems = Problem.objects.all()
		problems_solved_by_user = []
		if request.user.is_authenticated():
			problems_solved_by_user = Attempt.objects.filter(
				user = request.user,
				is_successful = True
			).values_list('problem__pk', flat=True).distinct()
		return render_to_response(
			'problems/list.html',
			{
				'problems': problems,
				'problems_solved_by_user': problems_solved_by_user
			},
			context_instance = RequestContext(request)
		)


class Single(View):
	def identify_problem(self, slug):
		"""
		Identifies the problem based on its slug.
		"""
		try:
			self.problem = Problem.objects.get(slug=slug)
		except Problem.DoesNotExist:
			raise Http404
	
	def get(self, request, slug):
		"""
		Renders a single problem.
		"""
		self.identify_problem(slug)
		return render_to_response(
			'problems/single.html',
			{
				'problem': self.problem
			},
			context_instance = RequestContext(request)
		)
	
	def post(self, request, slug):
		"""
		Handles challenge submission.
		"""
		self.identify_problem(slug)
		if not self.check_challenges(request):
			success = False
			message = _("You got it wrong.")
		else:
			success = True
			message = _("You got it right.")
		attempt = Attempt(
			problem = self.problem,
			user = request.user,
			is_successful = success
		)
		attempt.save()
		return render_to_response(
			'problems/single.html',
			{
				'problem': self.problem,
				'message': message,
				'success': success
			},
			context_instance = RequestContext(request)
		)
	
	def check_challenges(self, request):
		"""
		Checks whether the submitted answers are correct.
		"""
		for i in range(1, self.problem.number_of_challenges+1):
			name = 'challenge_' + str(i)
			if not all(k in request.POST for k in (name, name+'_answer')):
				return False
			try:
				challenge = ChallengeModel.objects.get(
					problem = self.problem,
					challenge = request.POST[name]
				)
			except ChallengeModel.DoesNotExist:
				return False
			if request.POST[name+'_answer'] != challenge.answer:
				return False
		return True


class Challenge(Single):
	def get(self, request, slug):
		"""
		Renders a challenge for the problem.
		"""
		self.identify_problem(slug)
		challenges = ChallengeModel.objects.filter(
			problem = self.problem
		).order_by('?')[:self.problem.number_of_challenges]
		return render_to_response(
			'problems/challenge.html',
			{
				'challenges': challenges
			},
			context_instance = RequestContext(request)
		)


class Simple(Single):
	def get(self, request, slug):
		"""
		Renders the problem in (almost) plain text.
		"""
		self.identify_problem(slug)
		return render_to_response(
			'problems/simple.html',
			{
				'problem': self.problem
			},
			context_instance = RequestContext(request)
		)


class Discussion(Single):
	def get(self, request, slug):
		"""
		Renders a problem's discussion.
		"""
		self.identify_problem(slug)
		return render_to_response(
			'problems/discussion.html',
			context_instance = RequestContext(request)
		)

