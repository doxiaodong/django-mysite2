# coding:utf-8
import datetime
from django.utils import timezone
# from DjangoUeditor.models import UEditorField
from django_markdown.models import MarkdownField
from django.db import models


# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField("文章类型", max_length=255)
    url = models.CharField("文章类型URL地址", max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    url = models.CharField("文章URL地址", max_length=100)
    title = models.CharField("标题", max_length=255)
    # content = UEditorField("内容", "100%", 120, imagePath="images/", filePath="files/", null=True, blank=True)
    content = models.TextField()
    # content = MarkdownField()
    create_time = models.DateTimeField("发布时间")
    # pic = models.ImageField("图片", null=True, blank=True, upload_to='article/')
    pic = models.CharField("图片", max_length=255, default='')
    hot = models.BooleanField("热门")
    is_up = models.BooleanField("置顶")

    def __str__(self):
        return self.title

    def was_created_recently(self):
        return self.create_time >= timezone.now() - datetime.timedelta(days=1)

    was_created_recently.admin_order_field = "create_time"
    was_created_recently.boolean = True
    was_created_recently.short_description = "最近发布"

    class Meta:
        ordering = ["-is_up", "-create_time"]

