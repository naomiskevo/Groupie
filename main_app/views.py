from django.shortcuts import render
from .models import Artist
import requests
import os




# Create your views here.
def show(request):
    print(request)
    # myKey = os.environ['SECRET_KEY']
    # appKey = os.environ['APP_ID']
    # req = requests.get(f"http://rest.bandsintown.com/artists/metallica?app_id={appKey}")
    # print('----------------<(^_^)>-----------------------')    
    # req = req.json()
    # print (req['name'])
    # print('----------------<(^_^)>-----------------------')
    # return render(request, 'index.html')
    # make request to eventul api

def home(request):
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://eventful.com/json/events?q=music&l=San+Diego")
    
    print(req)
    print('----------------<(^_^)>-----------------------')    
    req = req.json()
    # print (req['name'])
    print('----------------<(^_^)>-----------------------')
    print(req)
    return render(request, 'index.html')
    # make request to eventul api



def about(request):
    return render(request, 'about.html')

def artists_index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', { 'artists': artists })