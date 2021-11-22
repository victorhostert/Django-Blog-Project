from django.shortcuts import render
from blog.models import Artigo

def home(request):
    artigos = Artigo.objects.all().order_by('data')
    return render(request, 'index.html', {'artigos': artigos})