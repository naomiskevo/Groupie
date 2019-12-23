from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    # facebook = models.CharField(max_length=100)
    # bandsintown = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'artist_id': self.id})

class Event(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    sale = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

