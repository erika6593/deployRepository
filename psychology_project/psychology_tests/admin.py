from django.urls import path
from django.contrib import admin
from . models import (
    ProductPictures, ProductTypes, Quiz
)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'template_name')  # 正しいフィールド名を指定

# admin.site.register(Quiz, QuizAdmin)


admin.site.register(
    [ProductTypes, Quiz, ProductPictures,]
)


