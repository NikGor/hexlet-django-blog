# *hexlet_django_blog/article/views.py*
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from .models import Article


class IndexView(View):
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


class ArticleView(View):
    def get(self, request, tags, article_id):
        return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
