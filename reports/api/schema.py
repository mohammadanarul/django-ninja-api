from ninja import ModelSchema
from reports.models import PostReport


class PostReportSchema(ModelSchema):
    class Config:
        model = PostReport
        model_fields = ['id', 'post', 'text', 'status']
