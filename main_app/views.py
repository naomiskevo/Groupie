from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from .models import Artist, Event
import requests
import os





# Create your views here.
    

def artist_create(request):
  return render(request, 'detail.html')
  

def show(request):
    artist = request.POST['name_field']
    myKey = os.environ['SECRET_KEY']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://rest.bandsintown.com/artists/{artist}?app_id={appKey}")
    req = req.json()
    events = requests.get(f"http://rest.bandsintown.com/artists/{artist}/events?app_id={appKey}")
    events = events.json()
    artist = req
    print('----------------<(^_^)>-----------------------')
    return render(request, 'detail.html',{
      'artist': artist,
      'events': events
    })


def home(request):
    myKey = os.environ['SECRET_KEY']
    brite = os.environ['EVENTBRITE_TOKEN']
    req = requests.get(f"https://www.eventbriteapi.com/v3/users/me/?token={brite}")
    req = req.json()
    return render(request, 'index.html')


def events_index(request):
    return render(request, 'events/index.html')


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