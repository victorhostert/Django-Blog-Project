from django import forms
from django.db.models import fields
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'thumb', 'category']

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=80, required=True)

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['content']