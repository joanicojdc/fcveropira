from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse("Hello! This is the frontend app running.")


def home(request):
    return render(request, 'home.html')
def profile(request):
    return render(request, 'menu/profile.html')
def history(request):
    return render(request, 'menu/history.html')
def management(request):
    return render(request, 'menu/management.html')
def academy(request):
    return render(request, 'menu/academy.html')
def first_team(request):
    return render(request, 'menu/first_team.html')
def reserves(request):
    return render(request, 'menu/reserves.html')
def youth_team(request):
    return render(request, 'menu/youth_team.html')
def women_team(request):
    return render(request, 'menu/women_team.html')
def next_match(request):
    return render(request, 'menu/next_match.html')
def results(request):
    return render(request, 'menu/results.html')
def standings(request):
    return render(request, 'menu/standings.html')

def news(request):
    return render(request, 'menu/news.html')
def contact(request):
    return render(request, 'menu/contact.html')
