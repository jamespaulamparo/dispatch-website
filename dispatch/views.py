from django.shortcuts import render, get_object_or_404
from .models import Hero

# 1. HOMEPAGE (Random 4)
def home(request):
    # order_by('?') is the magic SQL command for "Randomize"
    # [:4] slices the list to only take the first 4 results
    heroes = Hero.objects.filter(status='Active').order_by('?')[:4]
    return render(request, 'index.html', {'heroes': heroes})

# 2. FULL ROSTER (Everyone)
def roster(request):
    # We pull the heroes grouped by their occupation
    context = {
        'branch_leaders': Hero.objects.filter(occupation='Branch Leader', status='Active'),
        'a_team': Hero.objects.filter(occupation='A-Team', status='Active'),
        'z_team': Hero.objects.filter(occupation='Z-Team', status='Active'),
    }
    return render(request, 'roster.html', context)

# 3. HERO DETAIL
def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    return render(request, 'hero_detail.html', {'hero': hero})