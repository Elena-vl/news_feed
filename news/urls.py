from django.urls import path

from . import views
from django.views.generic import ListView, DetailView
from news.models import Articles, Category

app_name = 'news'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
]