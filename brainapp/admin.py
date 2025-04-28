from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import MemoryGameResult, ReactionTestResult, TestInformation, UserResult, Questions, Presentation
from django import forms
from docx import Document
from django.core.files.base import ContentFile
import base64
import os

@admin.register(TestInformation)
class TestInformationAdmin(ModelAdmin):
    list_display = ["tes_direction"]
        
@admin.register(UserResult)
class AdminUserResult(ModelAdmin):
    list_display = ['user', "test", 'test_count', 'correct', 'wrong', 'ball']
    list_filter = ['user', "test"]

    def user_test_completed_display(self, obj):
        return "Tugallangan" if obj.user_test.completed else "Tugallanmagan"
    
    user_test_completed_display.short_description = "Test holati"

    class Media:
        js = "js/url_edit_userresult.js"
        
@admin.register(Questions) 
class QuestionAdmin(ModelAdmin) :
    list_display = ["test", "question", "answer_A", "answer_B", "answer_C", "answer_D", "correct", "image", "img"]

class MemoryGameResultAdmin(ModelAdmin):
    list_display = ('game_name', 'user', 'time', 'moves', 'difficulty', 'created_at')
    list_filter = ('difficulty', 'created_at')
    search_fields = ('user__username', 'game_name')

class SpeedMathResultAdmin(ModelAdmin):
    list_display = ('game_name', 'user', 'score', 'correct_answers', 'incorrect_answers', 'accuracy', 'difficulty', 'operation', 'created_at')
    list_filter = ('difficulty', 'operation', 'created_at')
    search_fields = ('user__username', 'game_name')

class ReactionTestResultAdmin(ModelAdmin):
    list_display = ('game_name', 'user', 'reaction_time', 'average_time', 'attempts', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'game_name')

admin.site.register(MemoryGameResult, MemoryGameResultAdmin)
admin.site.register(ReactionTestResult, ReactionTestResultAdmin)

@admin.register(Presentation)
class PresentetionAdmin(ModelAdmin) :
    list_display = ["title", "description", "file", "created_at"]
    list_filter = ["title", "created_at"]
    search_fields = ["title", "description"]