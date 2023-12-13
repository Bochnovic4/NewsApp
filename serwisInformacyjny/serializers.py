from rest_framework import serializers
from .models import Tag, Article, ArticleRating, Comment


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
