# coding:utf-8
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('账户增加', {
            'fields': ['sex', 'pic', 'nickname'],
        }),
    ]


# admin.site.register(User)
admin.site.register(Profile)