from django.shortcuts import render
from .models import Article

def home(request):
    artigos = Article.objects.all().order_by('date')
    return render(request, 'index.html', {'artigos': artigos})

def blog(request):
    artigos = Article.objects.all().order_by('date')
    return render(request, 'blog/blog.html', {'artigos': artigos})

def about(request):
    return render(request, 'blog/about.html')

def post(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'article': article})