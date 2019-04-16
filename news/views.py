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
    context_object_name = 'news_list'

    def get_queryset(self):
        """Return the last 20 published news."""
        return Articles.objects.all().order_by("-pub_date")[:20]

def detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'news/post.html', {'article': article})