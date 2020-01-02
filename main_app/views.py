from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import ModelFormMixin
from django.db import models
from .models import Artist, Event
from .forms import ArtistForm, EventForm
from django.contrib.auth.decorators import login_required
import requests
import os
import json


from django.contrib.auth.models import User




# Create your views here.

@login_required    
def add_artist(request, artist_id):
  form = ArtistForm(request.POST)
  if form.is_valid():
    new_artist = form.save(commit=False)
    new_artist.user = request.user
    new_artist.save()
  return redirect('/artists/')

@login_required
def add_event(request, event_id):
  form = EventForm(request.POST)
  if form.is_valid():
    new_event = form.save(commit=False)
    new_event.user = request.user
    new_event.save()
  return redirect('/events/')



def show(request):
    searched_artist = request.POST['name_field']
    appKey = os.environ['APP_ID']
    req = requests.get(f"http://rest.bandsintown.com/artists/{searched_artist}?app_id={appKey}")
    req = req.json()
    events = requests.get(f"http://rest.bandsintown.com/artists/{searched_artist}/events?app_id={appKey}")
    events = events.json()
    artist_form = ArtistForm()
    event_form = EventForm()
    return render(request, 'detail.html',{
      'artist': req,
      'events': events,
      'artist_form': artist_form,
      'event_form': event_form
    }) 




class ArtistDelete(DeleteView):
  model = Artist
  success_url = '/artists/'

class EventDelete(DeleteView):
  model = Event
  success_url = '/events/'


@login_required
def add_photo(request, event_id):
	# photo-file was the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, event_id=event_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('events/index.html', event_id=event_id)
  
def home(request):
  return render(request, 'index.html') 

@login_required
def events_index(request):
  events = Event.objects.all()
  return render(request, 'events/index.html', { 'events': events })

def about(request):
  return render(request, 'about.html')

@login_required
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