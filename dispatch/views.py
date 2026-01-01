from django.shortcuts import render, get_object_or_404
from .models import Hero
import random
from datetime import date

# 1. HOMEPAGE
def home(request):
    # 1. Get 4 random heroes for the visual display
    random_heroes = Hero.objects.filter(status='Active').order_by('?')[:4]
    
    # 2. Get the ACTUAL total count of active heroes for the stats number
    total_active_count = Hero.objects.filter(status='Active').count()
    
    # 3. Your News Feed Data
    news_feed = [
        # ... (keep your existing news dictionary items here) ...
    ]

    return render(request, 'index.html', {
        'heroes': random_heroes,
        'hero_count': total_active_count, # <--- PASSING THIS NEW VARIABLE
        'news_feed': news_feed
    })

# 2. FULL ROSTER
def roster(request):
    context = {
        'branch_leaders': Hero.objects.filter(occupation='Branch Leader', status='Active'),
        'a_team': Hero.objects.filter(occupation='A-Team', status='Active'),
        'z_team': Hero.objects.filter(occupation='Z-Team', status='Active'),
    }
    return render(request, 'roster.html', context)

# 3. HERO PUBLIC PROFILE (Updated from "Dossier")
def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, pk=hero_id)
    return render(request, 'hero_detail.html', {'hero': hero})

# 4. SUBSCRIPTION PLANS
def services(request):
    return render(request, 'services.html')