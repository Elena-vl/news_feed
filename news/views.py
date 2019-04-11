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

class ArticleDetailView(DetailView):
    model = Articles
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    # model = Articles
    # template_name = 'news/post.html'