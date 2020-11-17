from django.contrib import admin
from .models import Quiz, Question

# Register your models here.

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 4

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInLine,]


admin.site.register(Quiz, QuizAdmin)

admin.site.register(Question)