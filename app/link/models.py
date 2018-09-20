# coding:utf-8
from django.db import models


# Create your models here.


class Link(models.Model):
    title = models.CharField("友情链接Title", max_length=255)
    url = models.CharField("友情链接URL地址", max_length=255)
    type = models.CharField("友情链接类型", max_length=255)

    def __str__(self):
        return self.url

