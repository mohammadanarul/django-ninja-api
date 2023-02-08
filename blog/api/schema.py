from ninja import ModelSchema
from blog.models import Post, Comment


class BlogSchema(ModelSchema):
    class Config:
        model = Post
        model_fields = ['id', 'title', 'description', 'likes']


class CommentSchema(ModelSchema):
    class Config:
        model = Comment
        model_fields = ['id', 'post', 'text']
