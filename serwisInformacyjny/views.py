from rest_framework import generics
from .models import Tag, Article, ArticleRating, Comment
from .serializers import TagSerializer, ArticleSerializer, ArticleRatingSerializer, CommentSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleRatingListCreateView(generics.ListCreateAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer


class ArticleRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
