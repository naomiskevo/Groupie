from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from .models import Artist, Event
import requests
import os

from django.db import models
from django.contrib.auth.models import User



# Create your views here.
    
# def get_context_data(self, **kwargs):
#   user = User.objects.get(id=kwargs['user_id'])
#   do something with this user

def artist_create(request):
  user_id = request.user.id
  print(user_id)
  user = User.objects.get(id=user_id)
  bio = 'fake bio data'
  print(user)
  print('----------------<(^_^)>-----------------------')
  data = request.POST.copy()
  name = data.get('name')  #use this method for all form fields that are going into the model
  print(name)
  artist = Artist.objects.create(user_id=user_id, name=name, bio=bio)
  print(artist)
  return render(request, 'artists/index.html')


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

# https://Ticketmasterstefan-skliarovV1.p.rapidapi.com/searchEvents
def home(request):
  # Example: https://app.ticketmaster.com/discovery/v2/events.json?apikey=VN3z590lf4nzKObwvWNHmCnXUwY7WU6j
    myKey = os.environ['TICKET_MASTER']
    req = requests.get(f"https://app.ticketmaster.com/discovery/v2/events?apikey={myKey}&keyword=Music&locale=*")
    req = req.json()
    print('------------------<(O_O)>-----------------')
    # print(req)
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