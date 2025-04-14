from django.urls import path
from . import views

urlpatterns = [
    # Home and general pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # User authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    
    # Games
    path('games/', views.games_list, name='games_list'),
    path('games/memory/', views.memory_game, name='memory_game'),
    path('games/speed-math/', views.speed_math, name='speed_math'),
    path('games/reaction-test/', views.reaction_test, name='reaction_test'),
    path('games/results/', views.game_results_list, name='game_results_list'),
    
    # Game score saving
    path('games/save-memory-score/', views.save_memory_score, name='save_memory_score'),
    path('games/save-speed-math-score/', views.save_speed_math_score, name='save_speed_math_score'),
    path('games/save-reaction-test/', views.save_reaction_test, name='save_reaction_test'),
]
