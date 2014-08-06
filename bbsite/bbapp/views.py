from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from bbapp.models import News

# Create your views here.

def all_news(request):
	return render_to_response('all_news.html', {'all_news': News.objects.all()})

def single_news(request, news_id=1):
	return render_to_response('single_news.html', {'single_news': News.objects.get(id=news_id)})
