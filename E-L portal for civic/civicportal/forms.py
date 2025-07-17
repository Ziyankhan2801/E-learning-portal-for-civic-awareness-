
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Article, Video, Quiz

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_url']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']
