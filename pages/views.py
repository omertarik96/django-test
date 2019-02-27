from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home_view(request, *args, **kwargs):
    # data = get_html("https://httpbin.org/ip")
    return render(request, "home.html", {})


def get_html(url):
    payload = {'key': "978b0bd93acbe46a6b4d73729c5a94f1", 'url':
        url}

    r = requests.get('http://api.scraperapi.com', params=payload)

    return r.text
