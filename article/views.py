# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from article.models import Article,About
from datetime import datetime
from django.http import Http404
# Create your views here.
def home1(requset):
	post_lists=Article.objects.all()
	pos_a=[]
	for post_list in post_lists:
		pos_d=dict()
		pos_abc=post_list.content.split('.')[0]
		post_d={'title':post_list.title,'date_time':post_list.date_time,'category':post_list.category,'abstract':pos_abc,'id':post_list.id}
		pos_a.append(pos_d)
	return render_to_response('home1.html',{'post_list':pos_a})
	# return HttpResponse('Hello Boss!')
def detail(request,id):
	try:
		post=Article.objects.get(id=id)
	except Article.DoesNotExist:
		raise Http404
	# post=Article.objects.all()[int(my_args)]
	# str=('title=%s,category=%s,date_time=%s,content=%s'%(post.title,post.category,
	# 	post.date_time,post.content))
	return render(request,"post.html",{'post':post})
def test(request):
	return render_to_response('test.html',{'current_time':datetime.now()})
def home(requset):
	post_list=Article.objects.all()
	return render_to_response('home.html',{'post_list':post_list})
def about(request):
	about=About.objects.all()
	if not about:
		age_now=int(datetime.now().year)-int(1993)
		about=About(name='zxgao',sex='male',age=age_now,word='Just a man, just a fulture',intro='I\'m handsome, and a code')
		about.save()
	return render_to_response('about.html',{'about':about[0]})
def archives(request):
	try:
		post_list=Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	return render(request, "archives.html",{'post_list':post_list,'error':False})
def search_tag(request,tag):
	try:
		post_list=Article.objects.filter(category__iexact=tag)
	except Article.DoesNotExist:
		raise Http404
	return render(request, "tag.html",{'post_list':post_list})
