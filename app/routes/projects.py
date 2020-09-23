from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.auth import is_admin
from app.controllers.projects import (
    load_projects,
    add_project,
    delete_projects,
    get_project,
    update_project,
    delete_project
)


class Projects(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name', type=str, required=True, location='json')
        self.reqparse.add_argument(
            'description', type=str, location='json', default="")
        self.reqparse.add_argument(
            'stack', type=list, required=True, location='json')
        self.reqparse.add_argument(
            'links', type=dict, location='json', default={})
        self.reqparse.add_argument('thumbnail', type=str, location='json')

    def get(self):
        projects = load_projects()
        return make_response({'success': True, 'projects': projects})

    @jwt_required
    def post(self):
        identity = get_jwt_identity()
        if not is_admin(identity):
            return make_response({'success': False, 'message': 'unauthorized'}, 401)

        project_data = self.reqparse.parse_args()
        new_project = add_project(project_data)

        if not new_project:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'project': new_project}, 200)

    @jwt_required
    def delete(self):
        identity = get_jwt_identity()
        if not is_admin(identity):
            return make_response({'success': False, 'message': 'unauthorized'}, 401)

        total = delete_projects()
        return make_response({'success': True, 'total_deleted': total}, 200)


class Project(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('stack', type=list, location='json')
        self.reqparse.add_argument('links', type=dict, location='json')
        self.reqparse.add_argument('thumbnail', type=str, location='json')

    def get(self, id):
        project = get_project(id)
        if not project:
            return make_response({'success': False, 'message': 'project not found'}, 404)

        return make_response({'success': True, 'project': project})

    @jwt_required
    def put(self, id):
        identity = get_jwt_identity()
        if not is_admin(identity):
            return make_response({'success': False, 'message': 'unauthorized'}, 401)

        project = get_project(id)
        if not project:
            return make_response({'success': False, 'message': 'project not found'}, 404)

        args = self.reqparse.parse_args()
        if not update_project(id, args):
            return make_response({'success': False, 'message': 'couldn`t update resource'}, 500)

        updated = get_project(id)
        return make_response({'success': True, 'project': project})

    @jwt_required
    def delete(self, id):
        identity = get_jwt_identity()
        if not is_admin(identity):
            return make_response({'success': False, 'message': 'unauthorized'}, 401)

        project = get_project(id)
        if not project:
            return make_response({'success': False, 'message': 'project not found'}, 404)

        if not delete_project(id):
            return make_response({'success': False, 'message': 'couldn`t delete project'}, 500)

        return make_response({'success': True})
