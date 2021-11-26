from django.shortcuts import redirect, render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def home(request):
    articles = Article.objects.all().order_by('date')[::-1]
    return render(request, 'index.html', {'articles': articles})

def about(request):
    return render(request, 'blog/about.html')

def post(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/post.html', {'article': article})

@login_required(login_url="/auth/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = instance.slugify()
            instance.save()
            return redirect('blog:home')
    else:
        form = forms.CreateArticle()
    context = {'form': form}
    return render(request, 'blog/article_create.html', context)

@login_required(login_url="/auth/login/")
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES, instance=article) 
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:home')
    else:
        form = forms.CreateArticle()
    context = {'form': form}
    return render(request, 'blog/article_create.html', context)

@login_required(login_url="/auth/login/")
def article_delete_proceed(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {'article': article}
    return render(request, 'blog/article_delete_proceed.html', context)

@login_required(login_url="/auth/login/")
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('blog:home')