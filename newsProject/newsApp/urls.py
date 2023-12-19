from .views import (ArticleListCreateView, CommentCreateView,
                    ArticleLikeView, ArticleDislikeView, CreateArticleFromUrlView)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Articles API",
        default_version='v1',
        description="API for managing articles",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('articles/<int:pk>/like/', ArticleLikeView.as_view(), name='article-like'),
    path('articles/<int:pk>/dislike/', ArticleDislikeView.as_view(), name='article-dislike'),
    path('create-article-from-url/', CreateArticleFromUrlView.as_view(), name='create-article-from-url'),
]
