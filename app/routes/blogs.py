from flask import make_response
from flask_restful import Resource, reqparse
from app.controllers.blogs import (
    get_blogs,
    add_blog,
    delete_blogs
)


class Blogs(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, required=True, location='json')
        self.reqparse.add_argument(
            'body', type=str, required=True, location='json')
        self.reqparse.add_argument(
            'tags', type=list, default=[], location='json')

    def get(self):
        blogs = get_blogs()
        return make_response({'success': True, 'blogs': blogs}, 200)

    def post(self):
        args = self.reqparse.parse_args()
        new_blog = add_blog(args)

        if not new_blog:
            return make_response({'success': False, 'message': 'Couldn`t add blog'}, 500)

        return make_response({'success': True, 'blog': new_blog}, 200)

    def delete(self):
        if not delete_blogs():
            return make_response({'success': False, 'message': 'Couldn`t delete blog'}, 500)

        return make_response({'success': True}, 200)
