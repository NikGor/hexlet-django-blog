# hexlet_django_blog/views.py
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView


class IndexView(View):
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


class AboutView(TemplateView):
    template_name = 'about.html'
