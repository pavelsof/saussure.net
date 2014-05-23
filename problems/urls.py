from django.conf.urls import patterns, include, url

from problems.views import List
from problems.views import Single
from problems.views import Challenge
from problems.views import Discussion
from problems.views import Simple


urlpatterns = patterns('',
	url(r'^$', List.as_view()),
	url(r'^(?P<slug>\w+)/$', Single.as_view()),
	url(r'^(?P<slug>\w+)/challenge/$', Challenge.as_view()),
	url(r'^(?P<slug>\w+)/discussion/$', Discussion.as_view()),
	url(r'^(?P<slug>\w+)/simple/$', Simple.as_view()),
)

