# coding:utf-8
from django.contrib import admin
from .models import *


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        ('友情链接', {
            'fields': ['url']
        }),
        ('其他信息', {
            'fields': ['type', 'title'],
        }),
    ]

    list_display = ('url', 'type', 'title')


admin.site.register(Link, LinkAdmin)