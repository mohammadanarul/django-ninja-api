from typing import List
from ninja import Router
from django.shortcuts import get_object_or_404
from blog.models import Post
from reports.models import PostReport
from reports.api.schema import PostReportSchema

router = Router()


@router.get('/', response=List[PostReportSchema])
def post_reports(request):
    return PostReport.objects.all()


@router.post('/create/')
def posrt_report_create(request, payload: PostReportSchema):
    pl = payload.dict()
    post = get_object_or_404(Post, id=payload.post)
    pl['post'] = post
    PostReport.objects.create(**pl)
    return payload.dict()

