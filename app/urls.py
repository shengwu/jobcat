from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'jobcat.views.home'),
)
