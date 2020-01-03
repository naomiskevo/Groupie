from django.contrib import admin
from .models import Artist, Event, Photo

# Register your models here.
admin.site.register(Artist)
admin.site.register(Event)
admin.site.register(Photo)
