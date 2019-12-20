from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Artist
import requests
import os




# Create your views here.
def show(request):
    artist = request.POST['name_field']
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://rest.bandsintown.com/artists/{artist}?app_id={appKey}")
    req = req.json()
    events = requests.get(f"http://rest.bandsintown.com/artists/{artist}/events?app_id={appKey}")
    events = events.json()
    artist = req
    print (req['name'])
    print(events)
    return render(request, 'detail.html',{
      'artist': artist,
      'events': events
    })

def home(request):
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://eventful.com/json/events?q=music&l=TX&t=December+2019")
    print(req)
    print('----------------<(^_^)>-----------------------')    
    req = req.json()
    print('----------------<(^_^)>-----------------------')
    print(req)
    return render(request, 'index.html')
    # make a post request to eventbrite api req = requests.post()



def about(request):
    return render(request, 'about.html')

def artists_index(request):
    artists = Artist.objects.all()
    return render(request, 'artists/index.html', { 'artists': artists })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return render(request, 'index.html')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)