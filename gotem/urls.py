from django.conf.urls import patterns, url

from gotem import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^objective/new/$', views.objective_new, name='objective_new'),
	url(r'^objectives/$', views.objective_list, name='objective_list'),
)