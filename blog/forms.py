from django import forms
from . import models
import datetime

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'content', 'thumb']

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=80, required=False)