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
