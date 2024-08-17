import requests
from django.shortcuts import render

def home(request):
    api_key = 'bdef21726c8146c1a6890c5722972d5f'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    news_data = response.json()

    return render(request, 'home.html', {'news_data': news_data})
