from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')
	thumbnail = models.FileField(upload_to=get_upload_file_name, default="uploaded_files/default-img-news.jpg")

	def __unicode__(self):
		return self.title