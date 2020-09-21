from flask import make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from app.controllers.blogs import (
    get_blogs,
    add_blog,
    delete_blogs,
    get_blog,
    update_blog,
    delete_blog
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

    @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        new_blog = add_blog(args)

        if not new_blog:
            return make_response({'success': False, 'message': 'Couldn`t add blog'}, 500)

        return make_response({'success': True, 'blog': new_blog}, 200)

    @jwt_required
    def delete(self):
        if not delete_blogs():
            return make_response({'success': False, 'message': 'Couldn`t delete blog'}, 500)

        return make_response({'success': True}, 200)


class Blog(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('body', type=str, location='json')
        self.reqparse.add_argument('tags', type=list, location='json')

    def get(self, id):
        blog = get_blog(id)
        if not blog:
            return make_response({'success': False, 'message': 'blog not found'}, 404)
        return make_response({'success': True, 'blog': blog}, 200)

    def put(self, id):
        blog = get_blog(id)
        if not blog:
            return make_response({'success': False, 'message': 'blog not found'}, 404)

        args = self.reqparse.parse_args()
        updated_blog = update_blog(id, args)

        if not update_blog:
            return make_response({'success': False, 'message': 'couldn`t update blog'}, 500)

        return make_response({'success': True, 'blog': updated_blog}, 200)

    def delete(self, id):
        blog = get_blog(id)
        if not blog:
            return make_response({'success': False, 'message': 'blog not found'}, 404)

        if not delete_blog(id):
            return make_response({'success': False, 'message': 'couldn`t delete blog'}, 500)

        return make_response({'success': True}, 200)
