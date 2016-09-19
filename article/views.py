from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
def home(requset):
	post_list=Article.objects.all()
	return render_to_response('home.html',{'post_list':post_list})
	# return HttpResponse('Hello Boss!')
def detail(request,my_args):
	post=Article.objects.all()[int(my_args)]
	str=('title=%s,category=%s,date_time=%s,content=%s'%(post.title,post.category,
		post.date_time,post.content))
	return HttpResponse(str)
def test(request):
	return render_to_response('test.html',{'current_time':datetime.now()})
def home1(requset):
	post_list=Article.objects.all()
	return render_to_response('post.html',{'post_list':post_list})