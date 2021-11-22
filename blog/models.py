from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField()
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)
    #TODO:add thumb e author depois

    def __str__(self) -> str:
        return self.titulo

    #template filters
    def snippet(self):
        if len(self.conteudo) > 50:
            return self.conteudo[:50] + "..."
        else:
            return self.conteudo