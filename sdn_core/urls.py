from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dispatch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # NEW ROUTE FOR THE ROSTER
    path('roster/', views.roster, name='roster'), 
    
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]