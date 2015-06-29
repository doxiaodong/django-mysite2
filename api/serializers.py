from app.article.models import ArticleCategory
from rest_framework import serializers


class ArticleCategoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = ('url', 'name')