# coding:utf-8
# from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):

    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    third = models.CharField("第三方", max_length=255, default='none')
    nickname = models.CharField("昵称", max_length=255, default='darlin')
    sex = models.IntegerField('性别', default=0)
    # pic = models.ImageField('头像', upload_to='user/', default='user/favicon.png')
    pic = models.CharField("头像", max_length=255, default='static/assets/images/head/head.png')

    # third = models.CharField("第三方", max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'account_profile'