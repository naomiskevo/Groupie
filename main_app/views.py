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
    
# def add_artist(request, artist_id):
#   # create the ModelForm using the data in request.POST
#   form = ArtistForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the artist_id assigned
#     new_artist = form.save(commit=False)
#     new_artist.artist_id = artist_id
#     new_artist.save()
#   return redirect('artists/index.html', artist_id=artist_id)

# def artist_create(request):
#   user_id = request.user.id
#   print(user_id)
#   user = User.objects.get(id=user_id)
#   artist_bio = 'fake bio data'
#   print(user)
#   data = request.POST.copy()
#   artist_name = data.get('name')  
#   print(artist_name)
#   artist = Artist(name=artist_name, bio=artist_bio)
#   artist.save()
#   return render(request, 'artists/index.html')


def add_artist(request, artist_id):
  # create the custom ModelForm using the data in request.POST
  print('----------------------------<(^_^)>--------')
  form = ArtistForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form until the user_id is assigned
    new_artist = form.save(commit=False)
    # you have the user already (request.user), no need to get from the db
    new_artist.user = request.user
    new_artist.save()
  return redirect('/artists/index.html')



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
  
# =======
# # https://Ticketmasterstefan-skliarovV1.p.rapidapi.com/searchEvents
# def home(request):
#   # Example: https://app.ticketmaster.com/discovery/v2/events.json?apikey=VN3z590lf4nzKObwvWNHmCnXUwY7WU6j
#     myKey = os.environ['TICKET_MASTER']
#     req = requests.get(f"https://app.ticketmaster.com/discovery/v2/events?apikey={myKey}&keyword=Music&locale=*")
#     req = req.json()
#     print('------------------<(O_O)>-----------------')
#     return render(request, 'index.html')
# >>>>>>> bleeding-edge

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