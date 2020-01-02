from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('artists/', views.artists_index, name='index'),
    path('events/', views.events_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('detail', views.show, name='artist'),
    path('artists/<int:artist_id>/add_artist/', views.add_artist, name='add_artist'),
    path('events/<int:event_id>/add_event/', views.add_event, name='add_event'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist_delete'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='event_delete'),
]