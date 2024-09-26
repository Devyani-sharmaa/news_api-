from django.shortcuts import render
import requests
from django.http import HttpResponse
API_KEY='add98a6444e84b1a83e601b7965687ba'
# Create your views here.
def home(request):
    url=f'https://newsapi.org/v2/everything?q=tesla&from=2024-08-26&sortBy=publishedAt&apiKey={API_KEY}'
    response= requests.get(url)
    data=response.json()
    articles=data['articles']


    context={
        'articles': articles
    }
    return render(request,'news_api/home.html',context)




def all_user(request):
    return HttpResponse('RETURING URS')