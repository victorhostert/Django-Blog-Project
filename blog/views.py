from django.shortcuts import render
from .models import Artigo

def home(request):
    artigos = Artigo.objects.all().order_by('data')
    return render(request, 'index.html', {'artigos': artigos})

def blog(request):
    artigos = Artigo.objects.all().order_by('data')
    return render(request, 'blog/blog.html', {'artigos': artigos})

def about(request):
    return render(request, 'blog/about.html')

def post(request, slug):
    artigo = Artigo.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'artigo': artigo})