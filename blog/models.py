from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def create_default_category():
        if not Category.objects.all():
            Category.objects.create(name="No category")
        
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)
    category = models.ForeignKey(Category, default=None,on_delete=CASCADE)

    def __str__(self) -> str:
        return self.title

    # def title_search(self):
    #     return self.title.upper()

    def snippet(self):
        if len(self.content) > 50:
            return self.content[:50] + "..."
        else:
            return self.content

    def thumbnail(self):
        if self.thumb:
            return self.thumb
        else:
            return None

    def model_slugify(self):
        title: str = self.title
        slug = slugify(title)
        articles = Article.objects.all()
        number = 0
        for article in articles:
            if article.slug == slug:
                number += 1
                slug = slug + str(number)
        return slug


class Comment(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=CASCADE, related_name='comments')

    def __str__(self) -> str:
        return f'{self.author}: {self.content}'