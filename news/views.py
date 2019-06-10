from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Category, Articles
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render_to_response
import django_filters

# @login_required(login_url='/accounts/login/')

class IndexView(generic.ListView):
    template_name = 'news/posts.html'
    context_object_name = 'category_list'
    model = Category
    # paginate_by=1
    def get_queryset(self, *args, **kwargs):
        context = {}
        search_category = self.request.GET.get('q')
        if search_category is not None:
            list_category = Category.objects.filter(title__icontains=search_category)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            last_category = '?q=%s' % search_category

            current_page = Paginator(list_category, 10)

            page = self.request.GET.get('page')
            try:
                category_list = current_page.page(page)
            except PageNotAnInteger:
                category_list = current_page.page(1)
            except EmptyPage:
                category_list = current_page.page(current_page.num_pages)
        else:
            search_category = Category.objects.all()
            current_page = Paginator(search_category, 1)
            page = self.request.GET.get('page')
            try:
                category_list = current_page.page(page)
            except PageNotAnInteger:
                category_list = current_page.page(1)
            except EmptyPage:
                category_list = current_page.page(current_page.num_pages)
        return category_list

def detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'news/post.html', {'article': article})