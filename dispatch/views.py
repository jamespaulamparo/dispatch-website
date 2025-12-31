from django.shortcuts import render, get_object_or_404
from .models import Hero

def home(request):
    # Fetch active heroes
    heroes = Hero.objects.filter(status='Active')
    return render(request, 'index.html', {'heroes': heroes})

def hero_detail(request, hero_id):
    # Fetch hero details
    hero = get_object_or_404(Hero, pk=hero_id)
    return render(request, 'hero_detail.html', {'hero': hero})