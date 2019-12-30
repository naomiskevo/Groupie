from django.forms import ModelForm
from .models import Artist, Event

class ArtistForm(ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'image']


class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'tickets', 'date', 'image', 'location', 'city', 'event_url']

