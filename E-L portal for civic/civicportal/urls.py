
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/article/', views.article_upload, name='upload_article'),
    path('upload/video/', views.video_upload, name='upload_video'),
    path('upload/quiz/', views.quiz_upload, name='upload_quiz'),
]
