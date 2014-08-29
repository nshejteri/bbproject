from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	url(r'^$', 'bbapp.views.home', name='home'),
	url(r'^news/all$', 'bbapp.views.all_news'),
	url(r'^news/id/(?P<news_id>\d+)/$', 'bbapp.views.single_news'),
	url(r'^informations$', 'bbapp.views.informations'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




