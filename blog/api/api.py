from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from blog.api.schema import BlogSchema
from blog.models import Post

router = Router()


@router.get('/posts', response=List[BlogSchema])
def get_posts(request):
    return Post.objects.all()


@router.get('/posts/{post_id}', response=BlogSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@router.post('/posts/create/')
def get_posts(request, payload: BlogSchema):
    post = Post.objects.create(**payload.dict())
    return payload.dict()


@router.put('/posts/{post_id}')
def get_post(request, post_id: int, payload: BlogSchema):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return {"success": True, 'data': payload.dict()}
