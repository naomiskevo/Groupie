from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('artists/', views.artists_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('detail', views.show, name='artist'),
    
]