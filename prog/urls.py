from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^blog/', 'blog.views.display_meta', name='display_meta'),
	url(r'^nachni/', include('nachni.urls')),
    # Examples:
    # url(r'^$', 'prog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
