from flask import make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from app.controllers.projects import load_projects, add_project


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
        project_data = self.reqparse.parse_args()
        new_project = add_project(project_data)

        if not new_project:
            return make_response({'success': False}, 400)

        return make_response({'success': True, 'project': new_project}, 200)

    def delete(self):
        pass
