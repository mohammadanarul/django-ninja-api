from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/posts/')
def get_posts(request):
    return {'data': 'Hello world ninja', 'status': 200}