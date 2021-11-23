from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug:slug>/', views.post, name='post'),
]

urlpatterns += staticfiles_urlpatterns()
