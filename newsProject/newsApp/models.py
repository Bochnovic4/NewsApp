from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def add_like(self):
        self.likes += 1
        self.save()

    def add_dislike(self):
        self.dislikes += 1
        self.save()


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
