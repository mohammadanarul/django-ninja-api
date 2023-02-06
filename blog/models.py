from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    likes = models.PositiveBigIntegerField(default=0)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)

