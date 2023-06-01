"""hexlet_django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .article.views import ArticleView
from .views import IndexView

urlpatterns = [
    path("", lambda request: redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42})), name="index"),
    path('articles/<str:tags>/<int:article_id>/', ArticleView.as_view(), name='article'),
    path("admin/", admin.site.urls),
]
