from django.contrib import admin
from .models import MemoryGameResult, SpeedMathResult, ReactionTestResult

class MemoryGameResultAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'user', 'time', 'moves', 'difficulty', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('user__username', 'game_name')

class SpeedMathResultAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'user', 'score', 'correct_answers', 'incorrect_answers', 'accuracy', 'difficulty', 'operation', 'created_at')
    list_filter = ('difficulty', 'operation', 'created_at')
    search_fields = ('user__username', 'game_name')

class ReactionTestResultAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'user', 'reaction_time', 'average_time', 'attempts', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'game_name')

admin.site.register(MemoryGameResult, MemoryGameResultAdmin)
admin.site.register(SpeedMathResult, SpeedMathResultAdmin)
admin.site.register(ReactionTestResult, ReactionTestResultAdmin)
