from django.urls import path

from meusite.settings import MEDIA_ROOT, MEDIA_URL
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.article_create, name='create'),
    path('<slug:slug>/', views.post, name='post'),
    path('update/<slug:slug>', views.article_update, name='update'),
    path('delete_proceed/<slug:slug>/', views.article_delete_proceed, name='delete_proceed'),
    path('delete/<slug:slug>/', views.article_delete, name='delete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
