from django.http import HttpResponse
from django.views import View


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('article')
