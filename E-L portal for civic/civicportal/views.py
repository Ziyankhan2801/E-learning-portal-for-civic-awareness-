
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Article, Video, Quiz, QuizResult, Progress
from .forms import ArticleForm, VideoForm, QuizForm, UserRegisterForm

def home(request):
    return render(request, 'civicportal/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'civicportal/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'civicportal/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    articles = Article.objects.all()
    videos = Video.objects.all()
    quizzes = Quiz.objects.all()
    return render(request, 'civicportal/dashboard.html', {
        'articles': articles,
        'videos': videos,
        'quizzes': quizzes
    })

@login_required
def article_upload(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.uploaded_by = request.user
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'civicportal/article_form.html', {'form': form})

@login_required
def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.uploaded_by = request.user
            video.save()
            return redirect('dashboard')
    else:
        form = VideoForm()
    return render(request, 'civicportal/video_form.html', {'form': form})

@login_required
def quiz_upload(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = QuizForm()
    return render(request, 'civicportal/quiz_form.html', {'form': form})
