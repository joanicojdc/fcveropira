# frontend/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('history', views.history, name='history'),
    path('management', views.management, name='management'),
    path('academy', views.academy, name='academy'),
    path('first_team', views.first_team, name='first_team'),
    path('reserves', views.reserves, name='reserves'),
    path('youth_team', views.youth_team, name='youth_team'),
    path('women_team', views.women_team, name='women_team'),
    path('next_match', views.next_match, name='next_match'),
    path('results', views.results, name='results'),
    path('standings', views.standings, name='standings'), 
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
]