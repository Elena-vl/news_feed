from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.detail import DetailView
from .models import Category, Articles
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')

class IndexView(generic.ListView):
    template_name = 'news/posts.html'
    context_object_name = 'сategory_list'

    def get_queryset(self):
        return Category.objects.all()

def detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'news/post.html', {'article': article})