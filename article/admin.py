from django.contrib import admin
from article.models import Article
# Register your models here.
admin.site.register(Article)
import sys;

reload(sys);
sys.setdefaultencoding("utf8")