# coding:utf-8
from django.shortcuts import render
# from django.http import JsonResponse, HttpResponseNotAllowed
from app.code import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import simplejson
from django.core import serializers as core_serializers
# from django.contrib.auth.models import User
from ..account.models import Profile
from ..article.models import Article
from .models import Comment, SubComment
import uuid
from app.code import errorResponse


# Create your views here.
# @csrf_exempt
def add_reply(request, article):
    if request.method == 'POST':
        post_data = request.POST

        content = post_data.get('content', None)

        if request.user.username:

            if content == '':
                return errorResponse('NOT_ALLOWED_NULL_REPLY')

            else:
                url = str(uuid.uuid1())
                reply_time = timezone.now()
                user = Profile.objects.get(username=request.user.username)
                article = Article.objects.get(url=article)

                try:
                    comment = Comment(url=url,
                                      article=article,
                                      reply_user=user,
                                      content=content,
                                      reply_time=reply_time)
                except Exception as err:
                    print(err)
                    return errorResponse('SERVER_ERROR')

                comment.save()
                response = {
                    'comment': {
                        'replyUser': {
                            'pic': str(comment.reply_user.pic),
                            'username': comment.reply_user.username,
                            'nickname': comment.reply_user.nickname
                        },
                        'content': comment.content,
                        'time': comment.reply_time,
                        'url': comment.url
                    }
                }
                return JsonResponse(response)
        else:
            return errorResponse('LOGIN_FIRST')


# @csrf_exempt
def add_sub_reply(request, head):
    if request.method == 'POST':
        post_data = request.POST

        reply_object_str = post_data.get('reply_object', None)
        content = post_data.get('content', None)

        if request.user.username:

            if content == '' or reply_object_str == '':
                return errorResponse('NOT_ALLOWED_NULL_REPLY')
            else:
                reply_time = timezone.now()
                user = Profile.objects.get(username=request.user)

                reply_object = Profile.objects.get(username=reply_object_str)
                head = Comment.objects.get(url=head)

                try:
                    sub_comment = SubComment(head=head,
                                             reply_user=user,
                                             reply_object=reply_object,
                                             content=content,
                                             reply_time=reply_time)
                except Exception as err:
                    print(err)
                    return errorResponse('SERVER_ERROR')
                sub_comment.save()
                response = {
                    'subComment': {
                        'replyUser': {
                            'pic': str(sub_comment.reply_user.pic),
                            'username': sub_comment.reply_user.username,
                            'nickname': sub_comment.reply_user.nickname
                        },
                        'replyObject': {
                            'pic': str(sub_comment.reply_object.pic),
                            'username': sub_comment.reply_object.username,
                            'nickname': sub_comment.reply_object.nickname
                        },
                        'content': sub_comment.content,
                        'time': sub_comment.reply_time
                    }
                }
                return JsonResponse(response)

        else:
            return errorResponse('LOGIN_FIRST')
