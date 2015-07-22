from app.article.models import ArticleCategory, Article
from app.comments.models import Comment, SubComment
from app.account.models import Profile
from rest_framework import serializers


# user_info
class UserInfoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('username', 'nickname', 'pic')


# articles
class ArticleCategoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = ('url', 'name')


class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
    category = ArticleCategoriesSerializer()

    class Meta:
        model = Article
        fields = ('url', 'title', 'create_time', 'category')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    category = ArticleCategoriesSerializer()

    class Meta:
        model = Article
        fields = ('title', 'create_time', 'category', 'content')


# comments
class CommentsArticlesSeralizer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ('url',)


class CommentsUserSeralizer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('username', 'nickname', 'pic')


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    article = CommentsArticlesSeralizer()
    reply_user = CommentsUserSeralizer()

    class Meta:
        model = Comment
        fields = ('url', 'article', 'reply_user', 'content', 'reply_time', 'index')


class SubCommentsCommentsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('url',)


class SubCommentsSerializer(serializers.HyperlinkedModelSerializer):
    head = SubCommentsCommentsSerializer()
    reply_user = CommentsUserSeralizer()
    reply_object = CommentsUserSeralizer()

    class Meta:
        model = SubComment
        fields = ('head', 'reply_user', 'reply_object', 'content', 'reply_time')

