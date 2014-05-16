from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic.base import View

from users.models import User


class Registration(View):
	def dispatch(self, request, *args, **kwargs):
		"""
		Prevents authenticated users from coming this way.
		"""
		if request.user.is_authenticated():
			raise Http404
		return super(Registration, self).dispatch(request, *args, **kwargs)
	
	def get(self, request):
		"""
		Handles the GET request.
		"""
		return self.render_page(request)
	
	def post(self, request):
		"""
		Handles user registration.
		"""
		# input validation
		if not all(k in request.POST for k in ('email', 'password', 'password2')):
			return self.render_page(request, _("Please fill in all required fields."))
		try: validate_email(request.POST['email'])
		except ValidationError:
			return self.render_page(request, _("Real email is required."))
		try:
			User.objects.get(email=request.POST['email'])
		except User.DoesNotExist: pass
		else:
			return self.render_page(request, _("This email is already taken."))
		if request.POST['password2'] != request.POST['password']:
			return self.render_page(request, _("The two passwords do not match."))
		
		# create new user
		user = User.objects.create_user(request.POST['email'], request.POST['password'])
		if 'name' in request.POST:
			user.name = request.POST['name']
			user.save()
		
		# happy!
		user_ = authenticate(username=request.POST['email'], password=request.POST['password'])
		login(request, user_)
		return HttpResponseRedirect('/users/me')
	
	def render_page(self, request, message=None):
		"""
		Renders the registration page.
		"""
		return render_to_response(
			'users/registration.html',
			{
				'message': message
			},
			context_instance = RequestContext(request)
		)


class Login(View):
	def dispatch(self, request, *args, **kwargs):
		"""
		Prevents authenticated users from coming this way.
		"""
		if request.user.is_authenticated():
			raise Http404
		return super(Login, self).dispatch(request, *args, **kwargs)
	
	def get(self, request):
		"""
		Handles the GET request.
		"""
		return self.render_page(request)
	
	def post(self, request):
		"""
		Handles user authentication.
		"""
		try:
			user = authenticate(username=request.POST['email'], password=request.POST['password'])
		except:
			return self.render_page(request, _("No such user."))
		if user is None:
			return self.render_page(request, _("No such user."))
		if not user.is_active:
			return self.render_page(request, _("User account has been de-activated."))
		login(request, user)
		return HttpResponseRedirect('/users/me')
	
	def render_page(self, request, message=None):
		"""
		Renders the login page.
		"""
		return render_to_response(
			'users/login.html',
			{
				'message': message
			},
			context_instance = RequestContext(request)
		)


class Logout(View):
	def dispatch(self, request, *args, **kwargs):
		"""
		Prevents non-authenticated users from coming this way.
		"""
		if not request.user.is_authenticated():
			raise Http404
		return super(Logout, self).dispatch(request, *args, **kwargs)
	
	def get(self, request):
		"""
		De-authenticates the user.
		"""
		logout(request)
		return HttpResponseRedirect('/')


class Profile(View):
	def get(self, request, slug=None):
		"""
		Renders the user's profile.
		"""
		# identify user
		if slug is None:
			if request.user.is_authenticated():
				profile = request.user
			else:
				raise Http404
		else:
			try:
				profile = User.objects.get(slug=slug)
			except User.DoesNotExist:
				raise Http404
		
		# render the page
		return render_to_response(
			'users/profile.html',
			{
				'profile': profile
			},
			context_instance = RequestContext(request)
		)

