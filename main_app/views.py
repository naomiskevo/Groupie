from django.shortcuts import render
from django.http import HttpResponse

class Artist:
    def __init__(self, name):
        self.name = name

artists = [
    Artist('Justin Timberlake'),
    Artist('Chance the Rapper'),
    Artist('Glassing')
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def artists_index(request):
    return render(request, 'artists/index.html', { 'artists': artists })