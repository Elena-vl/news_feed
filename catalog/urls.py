from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>', views.detail_cat, name='detail_cat'),
    path('article/<int:article_id>/', views.detail, name='detail'),
]