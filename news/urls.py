from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/news/', views.get_news, name='get_news'),
]

