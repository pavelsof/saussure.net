from django.conf.urls import patterns, url

from users.views import Login
from users.views import Logout
from users.views import Profile
from users.views import Registration


urlpatterns = patterns('',
	url(r'^me/$', Profile.as_view()),
	url(r'^registration/$', Registration.as_view()),
	url(r'^login/$', Login.as_view()),
	url(r'^logout/$', Logout.as_view()),
	url(r'^(?P<slug>\w+)/$', Profile.as_view()),
)

