from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

def index(request):
    return render(request, 'catalog/homePage.html')

def detail_cat(request, category_id):
    return HttpResponse("You're looking at category %s." % category_id)

from .models import Articles
def detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'catalog/detail.html', {'article': article})
    # return HttpResponse(article)