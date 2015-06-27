# coding:utf-8
from django.contrib import admin
from .models import ArticleCategory, Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('标题', {
            'fields': ['title']
        }),
        ('其他信息', {
            'fields': ['url', 'category', 'create_time', 'content', 'hot'],
        }),
    ]

    list_display = ('title', 'create_time', 'was_created_recently')
    list_filter = ['create_time']
    search_fields = ['title']


admin.site.register(ArticleCategory)
admin.site.register(Article, ArticleAdmin)