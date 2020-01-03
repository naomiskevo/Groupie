from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'artist_id': self.id})

class Event(models.Model):
    name = models.CharField(max_length=100)
    tickets = models.URLField(max_length=250)
    image = models.URLField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    url= models.URLField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})



class Photo(models.Model):
  url = models.URLField(max_length=200)
  event = models.ForeignKey(Event, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for event_id: {self.event_id} @{self.url}"


