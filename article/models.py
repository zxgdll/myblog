#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.db import models
from django.core.urlresolvers import reverse
class Article(models.Model):
	title=models.CharField(max_length=100) #博客标题
	category=models.CharField(max_length=50,blank=True)
	date_time=models.DateTimeField(auto_now_add=True)
	content=models.TextField(blank=True,null=True)
	def get_absolute_url(self):
		path=reverse("detail",kwargs={'id':self.id})
		return "http://127.0.0.1:8000%s"%path
	def __unicode__(self):
		return self.title
	class Meta:
		ordering=['-date_time']
class About(models.Model):
	name=models.CharField(max_length=50)
	sex=models.CharField(max_length=10)
	age=models.IntegerField()
	word=models.CharField(max_length=100)
	intro=models.TextField(blank=True,null=True)
	def __unicode__(self):
		return self.name
		
		