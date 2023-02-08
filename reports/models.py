from django.db import models
from blog.models import Post
from reports.choices import ReportChoices


class PostReport(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    status = models.IntegerField(choices=ReportChoices.choices)
