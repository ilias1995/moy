from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'nachni.views.index', name='index'),
	url(r'^register/', 'nachni.views.register', name='register'),
	url(r'^login/', 'nachni.views.login', name='login'),
	url(r'^glavnoe/', 'nachni.views.glavnoe', name='glavnoe'),
    # Examples:
    # url(r'^$', 'prog.views.home', name='home'),
)