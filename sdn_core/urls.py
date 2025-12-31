from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dispatch import views

urlpatterns = [
    # 1. DJANGO ADMIN (Standard Setup)
    # We removed name='dispatch_admin' because it is invalid here.
    path('admin/', admin.site.urls),

    # 2. DASHBOARD
    path('', views.home, name='home'),

    # 3. HERO DETAIL
    path('hero/<int:hero_id>/', views.hero_detail, name='hero_detail'),

    # 4. LOGIN
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # 5. LOGOUT
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]