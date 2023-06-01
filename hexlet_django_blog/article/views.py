from django.http import HttpResponse
from django.views import View


class ArticleView(View):
    def get(self, request, tags, article_id, *args, **kwargs):
        return HttpResponse(f'Stатья номер {article_id}. Тег {tags}')
