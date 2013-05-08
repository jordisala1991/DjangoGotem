from django.conf.urls import patterns, url

from gotem import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	url(r'^objective/new/$', views.objective_new),
    url(r'^sprint/(?P<sprint_id>\d+)/$', views.show_sprint, name='show_sprint')
)