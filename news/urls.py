from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/news/', views.get_news, name='get_news'),

    # Technology endpoints
    path('technology/', views.technology, name='technology'),
    path('api/technology/', views.get_technology_news, name='get_technology_news'),
    
    # Startups endpoints
    path('startups/', views.startups, name='startups'),
    path('api/startups/', views.get_startups_news, name='get_startups_news'),
    
    # AI endpoints
    path('ai/', views.ai, name='ai'),
    path('api/ai/', views.get_ai_news, name='get_ai_news'),
    
    # Science endpoints
    path('science/', views.science, name='science'),
    path('api/science/', views.get_science_news, name='get_science_news'),
]

