from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.controllers.skills import (
    add_skill,
    fetch_skills,
    fetch_skill,
    update_skill_set,
    delete_skill_set
)


class Skills(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, location='json', required=True)
        self.reqparse.add_argument(
            'stack', type=list, location='json', required=True)

    @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        title = args.get('title')
        stack = args.get('stack')

        skill = add_skill(title, stack)
        if not skill:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'skill': skill}, 200)

    def get(self):
        skills = fetch_skills()

        if not skills:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'skills': skills}, 200)


class Skill(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'stack', type=list, required=True, location='json')
        self.reqparse.add_argument(
            'full', type=bool, default=False, location='json')

    def get(self, id):
        skill = fetch_skill(id)

        if not skill:
            return make_response({'success': False, 'message': 'not found'}, 404)

        return make_response({'success': True, 'skill': skill}, 200)

    @jwt_required
    def put(self, id):
        args = self.reqparse.parse_args()
        stack = args.get('stack')
        full = args.get('full')

        update = update_skill_set(id, stack, full)
        if not update:
            return make_response({'success': False, 'message': 'not found'}, 404)

        return make_response({'success': True}, 200)

    @jwt_required
    def delete(self, id):
        if not delete_skill_set(id):
            return make_response({'success': False, 'message': 'not found'}, 404)

        return make_response({'success': True}, 200)
