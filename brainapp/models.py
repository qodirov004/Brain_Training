from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

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

class TestInformation(models.Model):
    tes_direction = models.CharField(max_length=200, verbose_name="Test yo'nalishi")
    
    class Meta:
        verbose_name = "Test ma'lumoti"
        verbose_name_plural = "Test ma'lumotlari"
        
    def __str__(self):
        return self.tes_direction

class Questions(models.Model):
    CHOICES = [
        ('--', '--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]
    test = models.ForeignKey(to=TestInformation, on_delete=models.SET_NULL, null=True, verbose_name="Test")
    question = models.TextField(verbose_name="Savol")
    answer_A = models.CharField(max_length=255, verbose_name="A Javob")
    answer_B = models.CharField(max_length=255, verbose_name="B Javob")
    answer_C = models.CharField(max_length=255, verbose_name="C Javob")
    answer_D = models.CharField(max_length=255, verbose_name="D Javob")
    correct = models.CharField(max_length=2, choices=CHOICES, default="--", verbose_name="To'g'ri javob")
    image = models.ImageField(upload_to="photos/", verbose_name="Rasm", null=True, blank=True)
    img = models.BooleanField(verbose_name="Rasm mavjudmi", default=False)
    
    class Meta:
        verbose_name = "Test savollari"
        verbose_name_plural = verbose_name
        
    def __str__(self) -> str:
        return self.question[:20]

class UserAnswer(models.Model):
    CHOICES = [
        ('--', '--'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    ]
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, verbose_name="Foydalanuvchi")
    question = models.TextField(verbose_name="Savol")
    answer_A = models.CharField(max_length=255, verbose_name="A Javob")
    answer_B = models.CharField(max_length=255, verbose_name="B Javob")
    answer_C = models.CharField(max_length=255, verbose_name="C Javob")
    answer_D = models.CharField(max_length=255, verbose_name="D Javob")
    correct = models.CharField(max_length=2, choices=CHOICES, default="--", verbose_name="Tog'ri javob")
    answer = models.CharField(max_length=2, choices=CHOICES, default="--", verbose_name="Tanlagan javobi")

    def __str__(self) -> str:
        return self.answer
    
    class Meta:
        verbose_name = "Foydalanuvchi javoblari"
        verbose_name_plural = verbose_name

class UserTestTemp(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Ismi")
    test = models.ForeignKey(to=TestInformation, null=True, blank=True,  on_delete=models.SET_NULL)

class UserResult(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    test = models.ForeignKey(to = TestInformation, on_delete=models.CASCADE, verbose_name="Test")
    test_count = models.PositiveIntegerField(verbose_name="Savollar soni")
    correct = models.PositiveIntegerField(verbose_name="To'gri javoblar soni")
    wrong = models.PositiveIntegerField(verbose_name="Xato javoblar soni")
    ball = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Ball")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vaqti")
    
    def __str__(self) -> str:
        return f"{self.user.full_name} - {self.test.test_direction}"
    
    class Meta:
        verbose_name = "Foydalanuvchilar natijalari"
        verbose_name_plural = verbose_name
        
class Presentation(models.Model) :
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    file = models.FileField(upload_to="presentations/", verbose_name="Fayl")
    created_at = models.DateField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    
    class Meta : 
        verbose_name = "Prezentatsiya"
        verbose_name_plural = "Prezentatsiyalar"
        
    def __str__(self):
        return self.title