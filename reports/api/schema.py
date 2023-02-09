from ninja import ModelSchema, Schema
from reports.models import PostReport
from blog.api.schema import BlogSchemaID


class PostReportSchema(Schema):
    id: int = None
    post: int
    text: str
    status: int


class PostReportDefaultSchema(Schema):
    id: int
    post: BlogSchemaID = None
    text: str
    status: int

    # class Config:
    #     model = PostReport
    #     model_fields = ['id', 'post', 'text', 'status']
