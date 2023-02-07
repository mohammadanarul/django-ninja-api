from ninja import Schema


class BlogSchema(Schema):
    title: str
    description: str
    likes: int = 0


class BlogDetailSchema(Schema):
    id: int
    title: str
    description: str
    likes: int = 0


class CommentSchema(Schema):
    post_id: int
    text: str
