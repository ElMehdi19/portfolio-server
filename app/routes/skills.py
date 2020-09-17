from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.controllers.skills import add_skill, get_skills


class Skills(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, location='json', required=True)
        self.reqparse.add_argument(
            'stack', type=list, location='json', required=True)

    # @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        title = args.get('title')
        stack = args.get('stack')

        skill = add_skill(title, stack)
        if not skill:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'skill': skill}, 200)

    def get(self):
        skills = get_skills()

        if not skills:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'skills': skills}, 200)
