from ninja import ModelSchema, Schema

from blog.models import Comment, Post


class BlogSchemaID(Schema):
    id: int
    title: str


class BlogSchema(ModelSchema):
    class Config:
        model = Post
        model_fields = ['id', 'title', 'description', 'likes']


class CommentSchema(ModelSchema):
    class Config:
        model = Comment
        model_fields = ['id', 'post', 'text']
