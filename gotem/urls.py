from django.conf.urls import patterns, url

from gotem import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index')
)