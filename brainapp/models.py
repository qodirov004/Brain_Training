from django.db import models
from django.contrib.auth.models import User

class MemoryGameResult(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_name = models.CharField(max_length=100, default="Memory Game")
    time = models.CharField(max_length=10)  # Format: MM:SS
    moves = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{self.game_name} - {username} - {self.time} - {self.difficulty}"

class SpeedMathResult(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    OPERATION_CHOICES = [
        ('addition', 'Addition'),
        ('subtraction', 'Subtraction'),
        ('multiplication', 'Multiplication'),
        ('division', 'Division'),
        ('mixed', 'Mixed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_name = models.CharField(max_length=100, default="Speed Math")
    score = models.IntegerField()
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()
    accuracy = models.IntegerField()  # Percentage
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    operation = models.CharField(max_length=15, choices=OPERATION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{self.game_name} - {username} - Score: {self.score} - {self.difficulty}"

class ReactionTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    game_name = models.CharField(max_length=100, default="Reaction Test")
    reaction_time = models.IntegerField()  # In milliseconds
    attempts = models.IntegerField()
    average_time = models.IntegerField()  # Average reaction time in milliseconds
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f"{self.game_name} - {username} - Avg: {self.average_time}ms"
