from django.shortcuts import render
from .models import Artigo

def blog(request):
    artigos = Artigo.objects.all().order_by('data')
    return render(request, 'blog/blog.html', {'artigos': artigos})


def about(request):
    return render(request, 'blog/about.html')