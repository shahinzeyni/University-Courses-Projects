from django.shortcuts import render
from django.http import HttpResponse
from . import models

def all_articles(request):
    articles = models.Article.objects.all()
    return render(request, 'blogApp/index.html', {'articles' : articles})

def single_article(request, slug):
    article = models.Article.objects.get(slug=slug)
    return render(request, 'blogApp/detail.html', {'article' : article})
