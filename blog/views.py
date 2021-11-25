from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def home(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'index.html', {'articles': articles})

def blog(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'blog/blog.html', {'articles': articles})

def about(request):
    return render(request, 'blog/about.html')

def post(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'article': article})

@login_required(login_url="/auth/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #TODO: save both article and user in DB
            return redirect('blog:home')
    else:
        form = forms.CreateArticle()
    return render(request, 'blog/article_create.html', {'form': form})