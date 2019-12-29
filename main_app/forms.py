from django.forms import ModelForm
from .models import Artist, Event

class ArtistForm(ModelForm):
  class Meta:
    model = Artist
    fields = ['name', 'bio']


class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['name', 'venue', 'date', 'location', 'sale']

