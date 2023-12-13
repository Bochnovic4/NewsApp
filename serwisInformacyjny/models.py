from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ArticleRating(models.Model):
    LIKE_DISLIKE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=7, choices=LIKE_DISLIKE_CHOICES)

    def save(self, *args, **kwargs):
        if self.rating == 'like':
            self.article.likes += 1
        elif self.rating == 'dislike':
            self.article.dislikes += 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.rating == 'like':
            self.article.likes -= 1
        elif self.rating == 'dislike':
            self.article.dislikes -= 1
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.article.title} - {self.get_rating_display()}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title} - {self.content}"
