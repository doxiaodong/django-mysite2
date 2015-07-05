from app.article.models import ArticleCategory, Article
from rest_framework import serializers


class ArticleCategoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = ('url', 'name')


class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
    category = ArticleCategoriesSerializer()

    class Meta:
        model = Article
        fields = ('url', 'title', 'create_time', 'category')
