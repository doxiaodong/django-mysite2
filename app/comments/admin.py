# coding:utf-8
from django.contrib import admin
from .models import *


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('文章', {
            'fields': ['article']
        }),
        ('其他信息', {
            'fields': ['url', 'content', 'reply_time', 'reply_user'],
        }),
    ]

    list_display = ('content', 'reply_time', 'article', 'was_reply_recently')
    list_filter = ['reply_time']
    search_fields = ['article']


class SubCommentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('楼层', {
            'fields': ['head']
        }),
        ('其他信息', {
            'fields': ['content', 'reply_time', 'reply_user', 'reply_object'],
        }),
    ]

    list_display = ('content', 'reply_time', 'head', 'was_subreply_recently')
    list_filter = ['reply_time']
    search_fields = ['head']

admin.site.register(Comment, CommentAdmin)
admin.site.register(SubComment, SubCommentAdmin)