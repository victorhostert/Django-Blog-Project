from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Article, Category, Comment
from . import forms
from accounts.decorators import allowed_users


def home(request):
    try:
        articles = Article.objects.all().order_by('date')[::-1]
        paginator = Paginator(articles, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except TypeError:
        articles = None
    return render(request, 'index.html', {'articles': page_obj})

def about(request):
    return render(request, 'blog/about.html')

def post(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(article=article)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = request.POST.get('content')
            comment.article = article
            comment.author = request.user
            comment.save()
    else:
        form = forms.CommentForm()
    return render(request, 'blog/post.html', {'article': article, 'form': form, 'comments': comments})
def search(request):
    if request.method == 'POST':
        search = request.POST.get('search').lower()
        all_articles = Article.objects.all()
        articles = []
        for article in all_articles:
            if search in article.title.lower():
                articles.append(article)
            if search in article.content.lower():
                articles.append(article)
            if search in article.author.username.lower():
                articles.append(article)
            if search in article.category.name.lower():
                articles.append(article)

        articles = list(dict.fromkeys(articles))[::-1]

        return render(request, 'blog/search_results.html', {'articles': articles})
    else:
        form = forms.SearchForm()
        return render(request, 'blog/article_search.html', {'form': form})

@login_required(login_url="/auth/login/")
@allowed_users(allowed_roles=['admin'])
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.slug = instance.model_slugify()
            instance.save()
            return redirect('blog:home')
    else:
        Category.create_default_category()
        form = forms.CreateArticle()
    context = {'form': form}
    return render(request, 'blog/article_create.html', context)

@login_required(login_url="/auth/login/")
@allowed_users(allowed_roles=['admin'])
def article_update(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('blog:home')
    else:
        form = forms.CreateArticle(instance=article)
    context = {'article': article, 'form': form,}
    return render(request, 'blog/article_update.html', context)

@login_required(login_url="/auth/login/")
@allowed_users(allowed_roles=['admin'])
def article_delete_proceed(request, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {'article': article}
    return render(request, 'blog/article_delete_proceed.html', context)

@login_required(login_url="/auth/login/")
@allowed_users(allowed_roles=['admin'])
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('blog:home')