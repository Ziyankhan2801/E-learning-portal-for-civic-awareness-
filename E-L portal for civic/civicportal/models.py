from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Quiz(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField(choices=[
        (1, 'Option 1'),
        (2, 'Option 2'),
        (3, 'Option 3'),
        (4, 'Option 4')
    ])

    def __str__(self):
        return self.question

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now_add=True)

class QuizResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    selected_option = models.IntegerField()
    is_correct = models.BooleanField()
    attempted_at = models.DateTimeField(auto_now_add=True)
