from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings
import json

def index(request):
    """Render the main news page"""
    return render(request, 'news/index.html')

def get_news(request):
    """Proxy endpoint to fetch news from News API"""
    try:
        # Use the News API endpoint
        url = "https://newsapi.org/v2/everything"
        params = {
            'domains': 'techcrunch.com,thenextweb.com',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 10,  # Limit to 10 articles
            'language': 'en',
            'sortBy': 'publishedAt'
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0',  # Add User-Agent header
            'Accept': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        # Print response for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:500]}...")  # Print first 500 chars
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'status': 'error',
                'message': f'Error fetching news: {response.status_code}',
                'details': response.text
            }, status=500)
            
    except Exception as e:
        print(f"Error in get_news: {str(e)}")  # Print error for debugging
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
        }, status=500)
    

def technology(request):
    """Render the technology news page"""
    return render(request, 'news/technology.html')

def get_technology_news(request):
    """Proxy endpoint to fetch technology news from News API"""
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            'country': 'us',
            'apiKey': settings.NEWS_API_KEY,
            'category': 'technology',
            'pageSize': 10
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'status': 'error',
                'message': f'Error fetching technology news: {response.status_code}',
                'details': response.text
            }, status=500)
            
    except Exception as e:
        print(f"Error in get_technology_news: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
        }, status=500)

def startups(request):
    """Render the startups news page"""
    return render(request, 'news/startups.html')

def get_startups_news(request):
    """Proxy endpoint to fetch startup news from News API"""
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            'q': 'startups OR "startup funding" OR "new venture"',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 10,
            'language': 'en',
            'sortBy': 'publishedAt'
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'status': 'error',
                'message': f'Error fetching startup news: {response.status_code}',
                'details': response.text
            }, status=500)
            
    except Exception as e:
        print(f"Error in get_startups_news: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
        }, status=500)

def ai(request):
    """Render the AI news page"""
    return render(request, 'news/ai.html')

def get_ai_news(request):
    """Proxy endpoint to fetch AI news from News API"""
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            'q': 'artificial intelligence OR AI OR "machine learning" OR "deep learning"',
            'apiKey': settings.NEWS_API_KEY,
            'pageSize': 10,
            'language': 'en',
            'sortBy': 'publishedAt'
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'status': 'error',
                'message': f'Error fetching AI news: {response.status_code}',
                'details': response.text
            }, status=500)
            
    except Exception as e:
        print(f"Error in get_ai_news: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
        }, status=500)

def science(request):
    """Render the science news page"""
    return render(request, 'news/science.html')

def get_science_news(request):
    """Proxy endpoint to fetch science news from News API"""
    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            'country': 'us',
            'apiKey': settings.NEWS_API_KEY,
            'category': 'science',
            'pageSize': 10
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json'
        }
        
        response = requests.get(url, params=params, headers=headers)
        
        if response.status_code == 200:
            return JsonResponse(response.json())
        else:
            return JsonResponse({
                'status': 'error',
                'message': f'Error fetching science news: {response.status_code}',
                'details': response.text
            }, status=500)
            
    except Exception as e:
        print(f"Error in get_science_news: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': f'Error: {str(e)}',
        }, status=500)


