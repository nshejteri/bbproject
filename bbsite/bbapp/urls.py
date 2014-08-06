from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all$', 'bbapp.views.all_news'),
	url(r'^id/(?P<news_id>\d+)/$', 'bbapp.views.single_news'),
)




