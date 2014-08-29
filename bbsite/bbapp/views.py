from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.context_processors import csrf
import json
from django.core import serializers
from bbapp.models import News, Information
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	last_news = News.objects.order_by('-pub_date')[:4]
	last_informations = Information.objects.order_by('-pub_date')[:4]
	args = {}
	args.update(csrf(request))
	args['last_news'] = last_news
	args['last_informations'] = last_informations

	return render_to_response('index.html', args)

def all_news(request):
	return render_to_response('all_news.html', {'all_news': News.objects.all()})

def single_news(request, news_id=1):
	return render_to_response('single_news.html', {'single_news': News.objects.get(id=news_id)})

def single_information(request, information_id=1):
	return render_to_response('single_information.html', {'single_information': Information.objects.get(id=information_id)})

def informations(request):

	if request.method == "POST":
		offset = int(request.POST.get('offset'))
		limit = int(request.POST.get('limit'))
		infos = Information.objects.order_by('-pub_date')[offset:offset + limit]
		
	return render_to_response('ajax_informations.html', {'informations': infos})
