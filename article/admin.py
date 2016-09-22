from django.contrib import admin
from article.models import Article
from article.models import About
# Register your models here.
admin.site.register(Article)
admin.site.register(About)
import sys;

reload(sys);
sys.setdefaultencoding("utf8")