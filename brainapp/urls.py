from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('games/reaction-test/', views.reaction_test, name='reaction_test'),
    path('games/results/', views.game_results_list, name='game_results_list'),
    
    path('tests/', views.test_list, name='test_list'),
     path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    
    
    # Game score saving
    path('games/save-memory-score/', views.save_memory_score, name='save_memory_score'),
    path('games/save-reaction-test/', views.save_reaction_test, name='save_reaction_test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
