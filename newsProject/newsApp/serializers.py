from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text')


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('url', 'id', 'title', 'content', 'image', 'description', 'likes', 'dislikes', 'comments')

    url = serializers.URLField(required=False)
