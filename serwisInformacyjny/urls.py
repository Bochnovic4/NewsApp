from django.urls import path, re_path, include
from .views import (
    TagListCreateView, TagDetailView,
    ArticleListCreateView, ArticleDetailView,
    ArticleRatingListCreateView, ArticleRatingDetailView,
    CommentListCreateView, CommentDetailView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),

    path('ratings/', ArticleRatingListCreateView.as_view(), name='rating-list-create'),
    path('ratings/<int:pk>/', ArticleRatingDetailView.as_view(), name='rating-detail'),

    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
