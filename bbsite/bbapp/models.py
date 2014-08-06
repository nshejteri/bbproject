from django.db import models

# Create your models here.
class News(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.title