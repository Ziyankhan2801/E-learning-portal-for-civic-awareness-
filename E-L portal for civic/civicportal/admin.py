
from django.contrib import admin
from .models import User, Article, Video, Quiz, Progress, QuizResult
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Video)
admin.site.register(Quiz)
admin.site.register(Progress)
admin.site.register(QuizResult)
