# coding:utf-8
import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from ..article.models import Article
# from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):
    url = models.CharField("评论楼层URL地址，最好用日期", max_length=100)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reply_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    index = models.IntegerField("评论楼层，不要填写", null=True, blank=True)
    sub_comment = None

    content = models.TextField('内容')
    reply_time = models.DateTimeField('回复时间')

    def __str__(self):
        return self.content

    def was_reply_recently(self):
        return self.reply_time >= timezone.now() - datetime.timedelta(days=1)

    was_reply_recently.admin_order_field = "reply_time"
    was_reply_recently.boolean = True
    was_reply_recently.short_description = "最近评论"


class SubComment(models.Model):
    head = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reply_object = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reply_object", null=True, blank=True)

    content = models.TextField('内容')
    reply_time = models.DateTimeField('回复时间')

    def __str__(self):
        return self.content

    def was_subreply_recently(self):
        return self.reply_time >= timezone.now() - datetime.timedelta(days=1)

    was_subreply_recently.admin_order_field = "reply_time"
    was_subreply_recently.boolean = True
    was_subreply_recently.short_description = "最近回复"
