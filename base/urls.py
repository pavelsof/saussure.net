from django.conf.urls import patterns, include, url

from base.views import MainView


urlpatterns = patterns('',
	url(r'^$', MainView.as_view(), {'template_name': 'home.html'}),
	url(r'^meta/creators/$', MainView.as_view(), {'template_name': 'meta/creators.html'}),
)

