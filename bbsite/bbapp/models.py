from django.db import models
from time import time

def get_upload_file_name_news(instance, filename):
	return "uploaded_files/news/%s_%s" % (str(time()).replace('.', '_'), filename)

def get_upload_file_name_information(instance, filename):
	return "uploaded_files/informations/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')
	thumbnail = models.FileField(upload_to=get_upload_file_name_news, default="uploaded_files/news/default-img-news.jpg")

	def __unicode__(self):
		return self.title

class Information(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')
	thumbnail = models.FileField(upload_to=get_upload_file_name_information, default="uploaded_files/informations/default-img-information.jpg")