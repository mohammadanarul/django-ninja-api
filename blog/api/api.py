from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404
from blog.api.schema import BlogSchema, BlogDetailSchema
from blog.models import Post

blogApi = NinjaAPI()


@blogApi.get('/posts', response=List[BlogDetailSchema])
def get_posts(request):
    return Post.objects.all()


@blogApi.get('/posts/{post_id}', response=BlogDetailSchema)
def get_post(request, post_id: int):
    post = get_object_or_404(Post, id=post_id)
    return post


@blogApi.post('/posts/create/')
def get_posts(request, payload: BlogSchema):
    post = Post.objects.create(**payload.dict())
    return payload.dict()


@blogApi.put('/posts/{post_id}')
def get_post(request, post_id: int, payload: BlogSchema):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return {"success": True, 'data': payload.dict()}