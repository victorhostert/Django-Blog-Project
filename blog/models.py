from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #TODO:add author later

    def __str__(self) -> str:
        return self.title

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