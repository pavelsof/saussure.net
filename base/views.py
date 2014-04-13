from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View


class MainView(View):
	def get(self, request, template_name):
		"""
		Renders the template given.
		"""
		return render_to_response(
			template_name,
			context_instance = RequestContext(request)
		)

