from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'thumb']
    
# class UpdateArticle(forms.ModelForm)