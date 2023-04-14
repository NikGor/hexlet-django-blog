# *hexlet_django_blog/article/urls.py*
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:tags>/<int:article_id>/', views.ArticleView.as_view(), name='article'),
]
