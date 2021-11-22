from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.blog),
    path('about/', views.about),
    path('<slug:slug>/', views.details),
]

urlpatterns += staticfiles_urlpatterns()
