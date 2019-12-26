from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from django.db import models
from .models import Artist, Event
from .forms import ArtistForm
import requests
import os
import json


from django.contrib.auth.models import User




# Create your views here.
    
def add_artist(request, artist_id):
  # create the ModelForm using the data in request.POST
  form = ArtistForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the artist_id assigned
    new_artist = form.save(commit=False)
    new_artist.artist_id = artist_id
    new_artist.save()
  return redirect('artists/index.html', artist_id=artist_id)

def artist_create(request):
  user_id = request.user.id
  print(user_id)
  user = User.objects.get(id=user_id)
  artist_bio = 'fake bio data'
  print(user)
  data = request.POST.copy()
  artist_name = data.get('name')  
  print(artist_name)
  artist = Artist(name=artist_name, bio=artist_bio)
  artist.save()
  return render(request, 'artists/index.html')




def show(request):
    searched_artist = request.POST['name_field']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://rest.bandsintown.com/artists/{searched_artist}?app_id={appKey}")
    req = req.json()
    events = requests.get(f"http://rest.bandsintown.com/artists/{searched_artist}/events?app_id={appKey}")
    events = events.json()
    artist_form = ArtistForm()
    return render(request, 'detail.html',{
      'artist': req,
      'events': events,
      'artist_form': artist_form
    }) 


def home(request):
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