from rest_framework import generics
from rest_framework.response import Response
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from .utils import fetch_article_details
from bs4 import BeautifulSoup
import requests


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')

        if url:
            # Fetch article details from the URL
            title, image, description = fetch_article_details(url)
            data = {'title': title, 'image': image, 'description': description, **request.data}
        else:
            data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class ArticleLikeView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def patch(self, request, *args, **kwargs):
        article = self.get_object()
        article.add_like()
        serializer = self.get_serializer(article)
        return Response(serializer.data)


class ArticleDislikeView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def patch(self, request, *args, **kwargs):
        article = self.get_object()
        article.add_dislike()
        serializer = self.get_serializer(article)
        return Response(serializer.data)


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        article_id = self.kwargs.get('pk')

        if not article_id:
            return Response({'error': 'Provide a valid article_id'}, status=400)

        data = {'article': article_id, **request.data}

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(article_id=article_id)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class CreateArticleFromUrlView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def create(self, request, *args, **kwargs):
        url = request.data.get('url')

        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.RequestException as e:
                return Response({'error': f'Failed to fetch URL: {str(e)}'}, status=400)

            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else ''
            image = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else ''
            description = soup.find('meta', property='og:description')['content'] if soup.find('meta',
                                                                                               property='og:description') else ''

            data = {'url': url, 'title': title, 'image': image, 'description': description}
        else:
            # If URL is not provided, use the request data as it is
            data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
