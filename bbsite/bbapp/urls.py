from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'bbapp.views.home', name='home'),
	url(r'^news/all$', 'bbapp.views.all_news'),
	url(r'^news/id/(?P<news_id>\d+)/$', 'bbapp.views.single_news'),
)




